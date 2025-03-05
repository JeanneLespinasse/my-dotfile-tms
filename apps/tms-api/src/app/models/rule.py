from sqlalchemy import Column, String, JSON, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .base import Base

class Rule(Base):
    __tablename__ = "rule"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    scenario_id = Column(UUID, ForeignKey("scenario.id"))
    name = Column(String)
    json_logic = Column(JSON)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
