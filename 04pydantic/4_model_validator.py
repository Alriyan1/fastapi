from pydantic import BaseModel,EmailStr,AnyUrl,Field,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    Linkedin_url: AnyUrl
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age >60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.Linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

patient_info={'name':'alriyan','age':'67','email':'aba@hdfc.com','Linkedin_url':'http://linkedin.com/1234','weight':75.2,'married':True,'allergies':['pollen','dust'],
              'contact_details':{'number':'98796859','emergency':'977898'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)