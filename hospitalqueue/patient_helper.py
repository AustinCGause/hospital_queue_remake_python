from random import randint
from patient import Patient

@staticmethod
def _generate_id_number():
    randomly_generated_id = randint(100_000, 999_999)
    Patient.list_id_numbers.append(randomly_generated_id)
    return randomly_generated_id
