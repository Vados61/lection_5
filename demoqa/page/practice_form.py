from selene import have
from selene.support.shared.jquery_style import s, ss

from demoqa import media
from demoqa.controls import react_datepicker


def type_name(name):
    s('#firstName').set_value(name)


def type_last_name(last_name):
    s('#lastName').set_value(last_name)


def type_email(email):
    s('#userEmail').set_value(email)


def choose_gender(gender):
    ss('label').element_by(have.text(gender)).click()


def type_phone(phone):
    s('#userNumber').set_value(phone)


def choose_date_of_birth(day, month, year):
    react_datepicker.set_date('#dateOfBirthInput', day, month, year)


def choose_sabjects(subjects_list):
    for subject in subjects_list:
        s('#subjectsInput').type(subject).press_enter()


def choose_hobbies(hobbies):
    for hobbi in hobbies:
        ss('label').element_by(have.text(hobbi)).click()


def choose_photo(file_name):
    s('#uploadPicture').set_value(media.path(file_name))


def type_adress(adress):
    s('#currentAddress').set_value(adress)


def choose_state_and_city(state, city):
    s('#react-select-3-input').type(state).press_enter()
    s('#react-select-4-input').type(city).press_enter()


def check_submit_data(test_data):
    s('#submit').press_enter()
    ss('.table').all('td').even.should(have.exact_texts(test_data))
