from sqlalchemy import Column, String, Boolean, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .base import Base

class Scenario(Base):
    __tablename__ = "scenario"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    is_enabled = Column(Boolean)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
