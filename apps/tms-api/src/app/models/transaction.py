from sqlalchemy import Column, String, Integer, JSON, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .base import Base

class Transaction(Base):
    __tablename__ = "transaction"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_account = Column(String)
    target_account = Column(String)
    external_id = Column(String)
    amount = Column(Integer)
    currency = Column(String)
    meta_data = Column(JSON)
    created_at = Column(TIMESTAMP)
