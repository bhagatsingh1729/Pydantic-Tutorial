from pydantic import BaseModel
from typing import Literal

class Address(BaseModel):
    state:str
    city:str 
    pin:str

class Patient(BaseModel):

    name:str
    age:int
    gender: Literal['male','female','Male','Female','other']
    address:Address 

def show(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.gender)
    print(patient.address)

address_data = {'state':'Karnataka','city':'bangalore','pin':'560091'}
address = Address(**address_data)

patient_info = {'name':'Bhagat singh','age':21,'gender':'Male','address':address}
patient1  = Patient(**patient_info)

show(patient1)


