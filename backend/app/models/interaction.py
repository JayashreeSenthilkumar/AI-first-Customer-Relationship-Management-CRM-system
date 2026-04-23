from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String)
    topic = Column(String)
    follow_up = Column(String)
    summary = Column(String)
