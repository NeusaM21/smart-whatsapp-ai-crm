from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"), nullable=False)
    content = Column(String, nullable=False)
    sender = Column(String, nullable=False)  # user | bot
    created_at = Column(DateTime(timezone=True), server_default=func.now())