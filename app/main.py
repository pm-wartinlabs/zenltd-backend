from fastapi import FastAPI
from app.api.v1.routes import router as api_router
from app.core.config import settings
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

# Register routes
app.include_router(api_router, prefix="/api/v1")
