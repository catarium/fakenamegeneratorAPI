from dataclasses import dataclass
from parser_ import Parser


@dataclass
class Person:
    name: str
    address: str
    maiden_name: str
    ssn: str
    geo_cords: str
    phone: str
    country_code: str
    birthday: str
    age: str
    zodiac: str
    email_address: str
    username: str
    password: str
    website: str
    user_agent: str
    visa: str
    expires: str
    cvv2: str
    company: str
    occupation: str
    height: str
    weight: str
    blood_type: str
    ups: str
    western_union_mtcn: str
    moneygram_mtcn: str
    favorite_color: str
    vehicle: str
    GUID: str


def create_person(gender, name_lang, country):
    parser = Parser()
    data = parser.create_data(gender=gender, name_lang=name_lang, country=country)
    return Person(*data)
