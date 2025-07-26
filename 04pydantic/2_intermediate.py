from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='Name of the patient',description=
                                    'give the name of the patient in less than 50 chars',examples=['alriyan','khushi'])]
    age: int = Field(gt=0,lt=100)
    email: EmailStr
    Linkedin_url: AnyUrl
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=False,description='Is the patient married or not')]
    allergies:Annotated[Optional[List[str]],  Field(default=None,max_length=5)]
    contact_details: Dict[str,str]

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

patient_info={'name':'alriyan','age':30,'email':'aba@gmail.com','Linkedin_url':'http://linkedin.com/1234','weight':75.2,'married':True,'allergies':['pollen','dust'],
              'contact_details':{'number':'98796859'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)