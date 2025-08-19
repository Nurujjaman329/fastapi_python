from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth_routes, product_routes

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ecommerce Backend")

# Include routers
app.include_router(auth_routes.router)
app.include_router(product_routes.router)
