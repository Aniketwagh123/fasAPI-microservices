from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from models.employee import Employee
from config.settings import DATABASE_URL
from utils.rabbitmq import send_message


router = APIRouter()

client = MongoClient(DATABASE_URL)
db = client.employee_db
employee_collection = db.employees

@router.post("/employees", response_model=Employee)
def create_employee(employee: Employee):
    existing_employee = employee_collection.find_one({"id": employee.id})
    if existing_employee:
        raise HTTPException(status_code=400, detail="Employee already exists")
    
    employee_dict = employee.dict()
    employee_collection.insert_one(employee_dict)
    return employee

@router.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: str):
    employee = employee_collection.find_one({"id": employee_id})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return Employee(**employee)

@router.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: str, employee: Employee):
    existing_employee = employee_collection.find_one({"id": employee_id})
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    employee_collection.update_one({"id": employee_id}, {"$set": employee.dict()})
    return employee

@router.delete("/employees/{employee_id}", response_model=dict)
def delete_employee(employee_id: str):
    existing_employee = employee_collection.find_one({"id": employee_id})
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    employee_collection.delete_one({"id": employee_id})

    # Send a message to RabbitMQ to notify payroll service to delete payrolls
    send_message("payroll_delete_queue", {"employee_id": employee_id, "action": "delete"})
    
    return {"message": "Employee and associated payrolls deleted successfully"}
