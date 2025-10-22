from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator, EmailStr, confloat
from typing import Annotated, Optional
from fastapi.responses import JSONResponse
import json

app1 = FastAPI()

class Address(BaseModel):
    postal_code: int = Field(ge=10000, le=99999)
    street: str = Field(max_length=30, title="Street")
    city: str = Field(max_length=12)
    province: str = Field(max_length=15)
    country_of_stay: str = Field(max_length=15)

    @field_validator("province")
    @classmethod
    def validate_province(cls, value):
        provinces = ["Punjab","Sindh","kpk","Balochistan"]
        if value not in provinces:
            raise ValueError("Given Province is not valid")
        return value

class Student(BaseModel):
    name: Annotated[str, Field(max_length=15, title="Name Of Student")]
    Cnic: Annotated[str, Field(max_length=15, title="CNIC of Student", example="33100-1234567-1")]
    address: Address
    Guardian_name: Annotated[str, Field(max_length=15)]
    Department_name: Annotated[str, Field(max_length=20, example="AI")]
    Cgpa: Optional[Annotated[confloat(ge=0, le=4), Field(title="CGPA", example=3.75)]] = None
    email: EmailStr
    age: int = Field(ge=15, le=23)
    Matric_marks: confloat(ge=0, le=1100) = Field(title="Matriculation Marks")
    inter_marks: confloat(ge=0, le=1100) = Field(title="Intermediate Marks")

    @field_validator("Department_name")
    @classmethod
    def validate_dept(cls, value):
        dept_name = ["AI","CS","SE","EE"]
        if value not in dept_name:
            raise ValueError("Department Name is not Valid")
        return value

    @field_validator("Cnic")
    @classmethod
    def validate_cnic(cls, value):
        if len(value) != 15:
            raise ValueError("Length of CNIC is not valid")
        if value[5] != "-" or value[13] != "-":
            raise ValueError("Dashes are missing or not at correct places")
        return value

@app1.post("/create")
def create_student(student1: Student):
    data = student1.model_dump()
    with open('student_data.json', "w") as f:
        json.dump(data, f)
    return JSONResponse(status_code=201, content=["Student Created Successfully"])
