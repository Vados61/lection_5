from selene import have
from selene.support.shared.jquery_style import s, ss

from demoqa import media
from demoqa.controls import react_datepicker, radiobutton, checkboxes, dropdown


def type_name(name):
    s('#firstName').set_value(name)


def type_last_name(last_name):
    s('#lastName').set_value(last_name)


def type_email(email):
    s('#userEmail').set_value(email)


def choose_gender(gender):
    radiobutton.get_element('gender', gender).click()


def type_phone(phone):
    s('#userNumber').set_value(phone)


def choose_date_of_birth(day, month, year):
    react_datepicker.set_date('#dateOfBirthInput', day, month, year)


def choose_sabjects(subjects_list):
    for subject in subjects_list:
        s('#subjectsInput').type(subject).press_enter()


def choose_hobbies(hobbies):
    checkboxes.select_items(hobbies)


def choose_photo(file_name):
    s('#uploadPicture').set_value(media.path(file_name))


def type_address(address):
    s('#currentAddress').set_value(address)


def choose_state_and_city(state, city):
    dropdown.select_location(state, city)


def check_submit_data(test_data):
    s('#submit').press_enter()
    ss('.table').all('td').even.should(have.exact_texts(test_data))
