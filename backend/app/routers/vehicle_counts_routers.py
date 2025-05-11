from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.vehicle_counts_schemas import VehicleCountIn
from ..models.vehicle_counts_models import VehicleCount
from ..config import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/vehicle_count/")
def save_vehicle_count(data: VehicleCountIn, db: Session = Depends(get_db)):
    record = VehicleCount(
        vehicle_type=data.vehicle_type,
        direction=data.direction,
        count=data.count
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return {"status": "success", "id": record.id}
