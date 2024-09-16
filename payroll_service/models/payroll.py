from pydantic import BaseModel

class Payroll(BaseModel):
    id: str
    employee_id: str
    salary: float
    month: str
