from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .base import Base

class Alert(Base):
    __tablename__ = "alert"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    rule_id = Column(UUID, ForeignKey("rule.id"))
    status = Column(String)  # Could be an Enum if needed
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
