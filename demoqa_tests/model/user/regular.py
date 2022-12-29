from dataclasses import dataclass
from datetime import date


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    phone_number: int
    address: str
    state: str
    city: str
    gender: str
    hobbies: tuple
    subjects: tuple
    date_of_birth: date
    image: str
