from fastapi import FastAPI
from .config import Base, engine
from .routers.vehicle_counts_routers import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
