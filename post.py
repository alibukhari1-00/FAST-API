from fastapi import FastAPI,Path,HTTPException
from pydantic import BaseModel,Field,field_validator,EmailStr,AnyUrl,confloat
from fastapi.responses import JSONResponse
from typing import Annotated,Optional,List,Dict
import json


app1=FastAPI()
class address(BaseModel):
    postal_code:int =Field(max_length=5)
    street:str=Field(max_length=30,title="Street")
    city:str=Field(max_length=12)
    province:str=Field(max_length=15)
    countryOFstay:str=Field(max_length=15)
    @field_validator("province")
    @classmethod
    def validate(cls,value):
        province=["Punjab","Sindh","kpk","Balochistan"]
        if value not in province:
          raise ValueError("Given Province is not valid")
        
class Student(BaseModel):
    name:Annotated[str,Field(max_length=15,title="Name Of Student",description="Please Enter Your Name According to Nadra")]
    Cnic:Annotated[str,Field(max_length=15,title="CNIC of Student",description="Please Enter your Correct Cnic Number",example="33xxx-xxxxxxx-xx")]
    address:address
    Guardian_name:Annotated[str,Field(max_length=15,title="Guardian Name",description="Please Enter the Name of Your Guardian")]
    Department_name:Annotated[str,Field(max_length=20,title="Department Name",description="Please Enter Name of Your Department",example=["AI","CS","SE","EE"])]
    Cgpa:Optional[Annotated[float,Field(title="CGPA",description="Please enter your CGPA (0.0 - 4.0)",example=3.75)]]=None
    email:EmailStr
    age:int=Field(ge=15,le=23)
    Matric_marks:confloat=Field(ngte=1100,title="Matriculation Marks",description="Please Enter your Matric Marks")
    inter_marks:confloat=Field(ngte=1100,title="Intermediate Marks",description="Please Enter your Intermediate Marks")

    @field_validator("Department_name")
    @classmethod
    def validate_dept(cls,value):
        dept_name=["AI","CS","SE","EE"]
        if value not in dept_name:
            raise ValueError("Department Name is not Valid")
        return value
    
    @field_validator("Cnic")
    @classmethod
    def validate_cnic(cls,value):
        if len(value)!=15:
            raise ValueError("Lenght of Cnic is not valid !!!")
        if value[5]!="-":
            raise ValueError("Dashes are missing or not at correct Place")
        if value[13]!="-":
            raise ValueError("Dashes are missing or not at correct Place")
        return value


data={1:"ali", 2:"waqas", 3:"Mian", 4:"Suffian", 5:"Mohsin"}

@app1.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

@app1.get("/about")
def about():
    return {"message":"This is the about section of my api"}

@app1.get("/view")
def load_data():
    return data


@app1.get("/info/{id}")
def get_info(id: int=Path(...,description="Id is of the format 1 ,2 ,3 ",title="Patient Data ")):
    if id in data:
        return {"Info found Successfully ":data[id]}
    else:
        raise HTTPException(status_code=404,detail="Information not found")



@app1.post("/create")
def create_student(student1:Student):
    data=student1.model_dump()
    with open('student_data',"w") as f:
        json.dump(data,f)
    return JSONResponse(status_code=201,content=['Student Created Successfully'])