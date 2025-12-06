from pydantic import BaseModel, Field
from typing import List, Any

# --- Modelos aninhados para o payload do WhatsApp ---

class WhatsAppMessageContent(BaseModel):
    """Define a estrutura do campo 'text' da mensagem."""
    body: str

class WhatsAppMessageData(BaseModel):
    """Define a estrutura básica de uma mensagem de entrada."""
    # Usamos alias='from' pois 'from' é uma palavra reservada do Python
    from_field: str = Field(alias="from")
    text: WhatsAppMessageContent # Espera o corpo do texto

class WhatsAppChangeValue(BaseModel):
    """Define a estrutura do campo 'value' dentro de 'changes'."""
    # Lista de mensagens; pode estar vazia se for uma notificação de status
    messages: List[WhatsAppMessageData] = []
    
class WhatsAppChange(BaseModel):
    """Define a estrutura do campo 'changes'."""
    value: WhatsAppChangeValue

class WhatsAppEntry(BaseModel):
    """Define a estrutura do campo 'entry'."""
    # A lista de mudanças. Esperamos no mínimo 1 item.
    changes: List[WhatsAppChange] = Field(min_items=1) # <-- CORREÇÃO APLICADA AQUI

class WhatsAppWebhookIn(BaseModel):
    """
    Schema que representa o payload completo do webhook do WhatsApp.
    """
    object: str
    entry: List[WhatsAppEntry] = Field(min_items=1) # <-- CORREÇÃO APLICADA AQUI