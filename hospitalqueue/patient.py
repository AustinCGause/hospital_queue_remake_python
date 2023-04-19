from random import randint

class Patient:

    list_id_numbers = []
    patient_directory = {}

    def __init__(self, name: str, age: int, has_insurance = False) -> None:
        self.patient_name = name
        self.patient_age = age
        self.patient_has_insurance = has_insurance
        self.id_number = Patient._generate_id_number()
        
        Patient.patient_directory[self.id_number] = [self.patient_name, self.patient_age, 'Patient has insurance' if self.patient_has_insurance == True else 'Patient doesn\'t have insurance']

    def get_patient_name(self):
        return self.patient_name

    def get_patient_age(self):
        return self.patient_age

    def get_patient_id(self):
        return self.id_number
