from fastapi import APIRouter, HTTPException
from models.employee import Employee

router = APIRouter()

# Sample in-memory data store
employees = {}

@router.post("/employees", response_model=Employee)
def create_employee(employee: Employee):
    if employee.id in employees:
        raise HTTPException(status_code=400, detail="Employee already exists")
    employees[employee.id] = employee
    return employee

@router.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: str):
    if employee_id not in employees:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employees[employee_id]
