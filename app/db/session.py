from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from typing import AsyncGenerator

# A conexão deve usar a variável de ambiente segura
DATABASE_URL = settings.DATABASE_URL

# --- 1. CRIAÇÃO DO MOTOR ASSÍNCRONO ---
engine = create_async_engine(
    DATABASE_URL, 
    pool_pre_ping=True, 
    # **CORREÇÃO CRÍTICA:** Move statement_cache_size para connect_args.
    # Isso resolve o TypeError e o conflito com o PGBouncer/Supabase.
    connect_args={
        "statement_cache_size": 0 
    },
    echo=False,
)

# --- 2. CRIAÇÃO DA SESSÃO ASSÍNCRONA ---
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession, # Indica que esta é uma sessão assíncrona
    expire_on_commit=False,
)

# --- 3. DEPENDÊNCIA ASSÍNCRONA PARA AS ROTAS ---
def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Função geradora assíncrona para injeção de dependência no FastAPI.
    Garante que a sessão é fechada após o uso.
    """
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()