import asyncio
from app.db.session import engine
from app.db.base import Base

# Importar todos os models (MANTENHA PARA GARANTIR QUE OS MODELOS SEJAM CONHECIDOS PELA BASE)
from app.models.lead import Lead
from app.models.message import Message
from app.models.user import User


# A função agora deve ser assíncrona e usar o motor assíncrono
async def init_db():
    """
    Cria todas as tabelas no banco de dados Supabase (se não existirem)
    usando o motor assíncrono (AsyncEngine).
    """
    # Use engine.run() para executar comandos síncronos no motor assíncrono
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Função para executar a inicialização (útil para scripts fora do FastAPI)
def create_tables():
    """Executa a inicialização do DB de forma síncrona."""
    # Roda a função assíncrona no loop de eventos
    asyncio.run(init_db())