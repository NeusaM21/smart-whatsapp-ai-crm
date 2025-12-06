from fastapi import APIRouter, Request, HTTPException, status
from starlette.concurrency import run_in_threadpool
from sqlalchemy.future import select
from pydantic import ValidationError # Importação para lidar com a validação

# Importações de serviços, modelos e configuração
from app.services.ai_service import get_ai_response
from app.db.session import AsyncSessionLocal as SessionLocal
from app.models.lead import Lead
from app.core.config import settings
from app.schemas.whatsapp import WhatsAppWebhookIn # <-- NOVO: Importação do Schema

# Configuração do Router
router = APIRouter(prefix="/whatsapp", tags=["WhatsApp & CRM"])


# --- 1. Rota de Verificação (GET) ---
@router.get("/webhook", summary="Verify Webhook") # prefixo '/whatsapp' já está no router
async def verify_webhook(request: Request):
    """
    Verifica o token do Webhook para a Meta/WhatsApp.
    """
    VERIFY_TOKEN = settings.VERIFY_TOKEN

    try:
        mode = request.query_params.get("hub.mode")
        token = request.query_params.get("hub.verify_token")
        challenge = request.query_params.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("INFO: Webhook verificado com sucesso!")
            return challenge
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token de verificação inválido"
            )

    except Exception as e:
        print(f"ERRO DE VERIFICAÇÃO: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno na verificação do webhook"
        )


# --- 2. Rota de Mensagens (POST) ---
@router.post("/webhook", summary="Receive Message")
async def receive_message(payload: WhatsAppWebhookIn): # <-- CORREÇÃO: Usando Pydantic Model!
    """
    Recebe a mensagem do cliente, processa com IA,
    cadastra ou atualiza o Lead e retorna a resposta.
    """
    
    # NOTA: O payload JSON agora está validado e desserializado no objeto 'payload'
    
    # 1. VALIDAÇÃO E EXTRAÇÃO DE DADOS (USANDO O OBJETO PYDANTIC)
    try:
        # Tenta extrair a primeira mensagem de texto válida
        message_data = payload.entry[0].changes[0].value.messages[0]
        message_text = message_data.text.body
        from_number = message_data.from_field # 'from_field' é o alias para 'from'
        
    except (IndexError, AttributeError):
        # Isso acontece com notificações de status, leitura, ou outros tipos de mensagens
        return {
            "status": "ok",
            "message": "Evento ignorado (status/notificação ou formato de mensagem não suportado)."
        }

    # 2. CHAMADA DA IA (SÍNCRONA EXECUTADA EM THREAD)
    # A chamada aqui está correta, o problema está DENTRO do ai_service.py
    ai_response = await run_in_threadpool(
        get_ai_response,
        message_text
    )

    # 3. LÓGICA DE CRM (BANCO DE DADOS)
    async with SessionLocal() as db:

        result = await db.execute(
            select(Lead).where(Lead.phone == from_number)
        )
        lead = result.scalar_one_or_none()

        if lead is None:
            new_lead = Lead(
                name=f"Lead {from_number}",
                phone=from_number,
                message_history=f"Cliente: {message_text}\nIA: {ai_response}",
                status="new"
            )

            db.add(new_lead)
            print(f"INFO: Novo lead criado: {from_number}")

        else:
            lead.message_history = (
                (lead.message_history or "")
                + f"\nCliente: {message_text}\nIA: {ai_response}"
            )
            print(f"INFO: Histórico de lead atualizado: {from_number}")

        await db.commit()

    # 4. RESPOSTA FINAL
    return {
        "status": "ok",
        "ai_response": ai_response,
        "lead_phone": from_number,
        "action": "Lead processado e resposta da IA gerada."
    }