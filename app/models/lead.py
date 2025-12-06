from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True) # Sugestão: adicione 'unique=True'
    service = Column(String, nullable=True)
    status = Column(String, default="new")
    
    # NOVAS COLUNAS:
    message_history = Column(String, nullable=True) # Para salvar a conversa inteira
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) # Para rastrear a última interação

    created_at = Column(DateTime(timezone=True), server_default=func.now())