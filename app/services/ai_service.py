from google import genai
from google.genai.types import Content, Part # 1. Adicionado
from app.core.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

SYSTEM_PROMPT = (
    "Você é um assistente de vendas e atendimento cordial e profissional "
    "para o negócio 'Smart WhatsApp CRM'. Sua missão é qualificar o lead "
    "e agendar um serviço. Responda brevemente, mantendo a conversa "
    "focada em obter o nome completo e o serviço de interesse."
)

def get_ai_response(user_message: str) -> str:
    try:
        full_prompt = f"{SYSTEM_PROMPT}\n\nMensagem do cliente: {user_message}"

        # 2. CORREÇÃO: Usando objetos tipados Content e Part
        # O Part.from_text recebe apenas o texto, eliminando o erro.
        content = Content(
            role="user",
            parts=[
                Part.from_text(text=full_prompt)
            ]
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[content] # Passando a lista de objetos Content
        )

        return response.text

    except Exception as e:
        print(f"Erro ao chamar a API Gemini: {e}")
        return "Desculpe, estou com problemas técnicos no momento. Tente novamente mais tarde."