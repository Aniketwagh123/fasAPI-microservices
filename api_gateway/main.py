from fastapi import FastAPI
from routes import gateway

app = FastAPI()

# Include the gateway routes
app.include_router(gateway.router)
