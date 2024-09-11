from fastapi import FastAPI
from routes import employee

app = FastAPI()

# Include the employee routes
app.include_router(employee.router)
