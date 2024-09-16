from fastapi import FastAPI
from routes import payroll

app = FastAPI()

# Include the payroll routes
app.include_router(payroll.router)
