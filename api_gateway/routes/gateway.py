from fastapi import APIRouter, HTTPException
from httpx import AsyncClient
from config.settings import EMPLOYEE_SERVICE_URL, PAYROLL_SERVICE_URL

router = APIRouter()
client = AsyncClient()

@router.get("/employees/{employee_id}")
async def get_employee(employee_id: str):
    response = await client.get(f"{EMPLOYEE_SERVICE_URL}/employees/{employee_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@router.post("/employees")
async def create_employee(employee: dict):
    response = await client.post(f"{EMPLOYEE_SERVICE_URL}/employees", json=employee)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@router.get("/payrolls/{payroll_id}")
async def get_payroll(payroll_id: str):
    response = await client.get(f"{PAYROLL_SERVICE_URL}/payrolls/{payroll_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@router.post("/payrolls")
async def create_payroll(payroll: dict):
    response = await client.post(f"{PAYROLL_SERVICE_URL}/payrolls", json=payroll)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)
