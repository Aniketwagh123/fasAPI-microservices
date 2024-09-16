from fastapi import APIRouter, HTTPException
from httpx import AsyncClient
from pydantic import BaseModel
from config.settings import EMPLOYEE_SERVICE_URL, PAYROLL_SERVICE_URL

router = APIRouter()
client = AsyncClient()

class Employee(BaseModel):
    id: str
    name: str
    position: str

class Payroll(BaseModel):
    id: str
    employee_id: str
    salary: float
    month: str


@router.post("/employees", response_model=Employee)
async def create_employee(employee: Employee):
    response = await client.post(f"{EMPLOYEE_SERVICE_URL}/employees", json=employee.dict())
    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@router.get("/employees/{employee_id}", response_model=Employee)
async def get_employee(employee_id: str):
    response = await client.get(f"{EMPLOYEE_SERVICE_URL}/employees/{employee_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@router.put("/employees/{employee_id}", response_model=Employee)
async def update_employee(employee_id: str, employee: Employee):
    response = await client.put(f"{EMPLOYEE_SERVICE_URL}/employees/{employee_id}", json=employee.dict())
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@router.delete("/employees/{employee_id}", response_model=dict)
async def delete_employee(employee_id: str):
    response = await client.delete(f"{EMPLOYEE_SERVICE_URL}/employees/{employee_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@router.post("/payrolls", response_model=Payroll)
async def create_payroll(payroll: Payroll):
    response = await client.post(f"{PAYROLL_SERVICE_URL}/payrolls", json=payroll.dict())
    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@router.get("/payrolls/{payroll_id}", response_model=Payroll)
async def get_payroll(payroll_id: str):
    response = await client.get(f"{PAYROLL_SERVICE_URL}/payrolls/{payroll_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@router.put("/payrolls/{payroll_id}", response_model=Payroll)
async def update_payroll(payroll_id: str, payroll: Payroll):
    response = await client.put(f"{PAYROLL_SERVICE_URL}/payrolls/{payroll_id}", json=payroll.dict())
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@router.delete("/payrolls/{payroll_id}", response_model=dict)
async def delete_payroll(payroll_id: str):
    response = await client.delete(f"{PAYROLL_SERVICE_URL}/payrolls/{payroll_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)