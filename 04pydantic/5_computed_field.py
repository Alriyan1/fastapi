from pydantic import BaseModel,EmailStr,AnyUrl,Field,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    Linkedin_url: AnyUrl
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)

        return bmi
    

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.Linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('BMI',patient.calculate_bmi)
    print('Inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

patient_info={'name':'alriyan','age':'30','email':'aba@hdfc.com','Linkedin_url':'http://linkedin.com/1234','weight':75.2,'height':1.72,'married':True,'allergies':['pollen','dust'],
              'contact_details':{'number':'98796859'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)