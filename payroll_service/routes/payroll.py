from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from models.payroll import Payroll
from config.settings import DATABASE_URL

router = APIRouter()

client = MongoClient(DATABASE_URL)
db = client.payroll_db
payroll_collection = db.payrolls

@router.post("/payrolls", response_model=Payroll)
def create_payroll(payroll: Payroll):
    existing_payroll = payroll_collection.find_one({"id": payroll.id})
    if existing_payroll:
        raise HTTPException(status_code=400, detail="Payroll entry already exists")
    
    payroll_dict = payroll.dict()
    payroll_collection.insert_one(payroll_dict)
    return payroll

@router.get("/payrolls/{payroll_id}", response_model=Payroll)
def get_payroll(payroll_id: str):
    payroll = payroll_collection.find_one({"id": payroll_id})
    if not payroll:
        raise HTTPException(status_code=404, detail="Payroll entry not found")
    
    return Payroll(**payroll)

@router.put("/payrolls/{payroll_id}", response_model=Payroll)
def update_payroll(payroll_id: str, payroll: Payroll):
    existing_payroll = payroll_collection.find_one({"id": payroll_id})
    if not existing_payroll:
        raise HTTPException(status_code=404, detail="Payroll entry not found")
    
    payroll_collection.update_one({"id": payroll_id}, {"$set": payroll.dict()})
    return payroll

@router.delete("/payrolls/{payroll_id}", response_model=dict)
def delete_payroll(payroll_id: str):
    existing_payroll = payroll_collection.find_one({"id": payroll_id})
    if not existing_payroll:
        raise HTTPException(status_code=404, detail="Payroll entry not found")
    
    payroll_collection.delete_one({"id": payroll_id})
    return {"message": "Payroll entry deleted successfully"}
