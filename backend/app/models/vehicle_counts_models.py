from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..config import Base

class VehicleCount(Base):
    __tablename__ = "vehicle_counts"
    id = Column(Integer, primary_key=True, index=True)
    vehicle_type = Column(String(32))
    direction = Column(String(8))
    count = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
