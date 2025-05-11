from pydantic import BaseModel

class VehicleCountIn(BaseModel):
    vehicle_type: str
    direction: str
    count: int
