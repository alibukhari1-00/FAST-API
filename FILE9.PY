from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Student(BaseModel):
    name:Annotated[str,Field(max_length=30,title="Name of Student",description="Please enter the correct name of student",examples=["Ali","NAWAB"])]
    linkedin_url:Optional[AnyUrl]
    age:int =Field(gt=0,lt=39)
    height:Optional[float]=None
    Dept:Annotated[str,Field(max_lenght=10,default=None)]
    courses:List[str]
    email:EmailStr
    contact_details:Dict[str,str]

    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        valid_domains=["hbl.com","mcb.com"]
        domain_name=value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError("This Extension is not Supported")
        return value

def insert_student_data(std1:Student ):
    print(std1.age)
    print(std1.linkedin_url)
    print(std1.name)
    print(std1.height)
    print(std1.Dept)
    print(std1.courses)
    print(std1.email)
    print(std1.contact_details)


student_info={"name":"Ali","linkedin_url":"https://Linkedin","age":22,"Dept":'AI',"courses":["CV","MlOPS","PPIT","NLP"],"email":"ali@hbl.com","contact_details":{"HomePhone":"+92-3337-919766","OfficeNumber":"+92-332-000766","Email":"i.alibukhari1@gmail.com"}}
std1=Student(**student_info)
insert_student_data(std1)
    