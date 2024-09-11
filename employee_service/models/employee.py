from pydantic import BaseModel

class Employee(BaseModel):
    id: str
    name: str
    position: str
    salary: float
