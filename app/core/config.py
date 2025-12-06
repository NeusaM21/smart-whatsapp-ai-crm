from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

# 1. Definição das Configurações
class Settings(BaseSettings):
    """
    Carrega as variáveis de ambiente do arquivo .env
    e as valida.
    """
    model_config = SettingsConfigDict(
        # Especifica o arquivo .env a ser carregado
        env_file=".env",
        # Adiciona o protocolo 'postgresql+asyncpg' para o Pydantic entender
        # sem dar erro de validação (embora o SQLAlchemy use o driver)
        env_ignore_default=True
    )

    # Configurações do Banco de Dados
    DATABASE_URL: str
    
    # Configurações da IA
    GEMINI_API_KEY: str

    # Configurações do Projeto (opcional, mas bom ter)
    PROJECT_NAME: str = "Smart WhatsApp AI CRM"
    PROJECT_VERSION: str = "1.0.0"


# 2. Instância Única (Singleton)
# Usando @lru_cache para garantir que a classe Settings seja carregada
# apenas uma vez (singleton), otimizando a performance.
@lru_cache()
def get_settings():
    """Retorna uma instância única da classe Settings."""
    return Settings()

# Configuração global que você importará nos outros arquivos
settings = get_settings()