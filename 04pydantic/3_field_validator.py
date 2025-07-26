from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
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

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age',mode='after')
    @classmethod
    def validation_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age should be in 0 to 100')


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

patient_info={'name':'alriyan','age':'30','email':'aba@hdfc.com','Linkedin_url':'http://linkedin.com/1234','weight':75.2,'married':True,'allergies':['pollen','dust'],
              'contact_details':{'number':'98796859'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)