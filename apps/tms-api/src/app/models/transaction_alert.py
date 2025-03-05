from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from .base import Base

class TransactionAlert(Base):
    __tablename__ = "transaction_alert"
    
    alert_id = Column(UUID, ForeignKey("alert.id"), primary_key=True)
    transaction_id = Column(UUID, ForeignKey("transaction.id"), primary_key=True)
