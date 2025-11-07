from pydantic import BaseModel,Field,EmailStr,AnyUrl
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="Name of the patient",description="you write the name of the patient under 50 characters",examples=['bhagat singh','angad'])]
    age:int = Field(gt=0,lt=100,strict=True)
    Email:EmailStr
    Linkedin:AnyUrl
    weight:Annotated[float,Field(strict=True,gt=0)]
    contact:Annotated[Optional[Dict[str,str]],Field(default=None,title="contack details",description="contact details of the patient")]
    allergies:Annotated[List[str],Field(default=None,description="allergies of the patient are mentioned here",max_length=5)]
    marrage:Annotated[Optional[bool],Field(default=None,description="marrital status of the patient")]

def insert_data(Patient:Patient):
    print(Patient)
    print("inserted")

patient_data = {'name':'Bhagat singh','age':20,'weight':68,'allergies':['a1','b1'],'Email':'abc@gmail.com','Linkedin':'http://linkedin.com/1003','contact':{'number':'9380271906'}}
patient1 = Patient(**patient_data)

insert_data(patient1)