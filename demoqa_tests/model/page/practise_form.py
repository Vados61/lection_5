from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from demoqa_tests.media import path_to_file


class Page:

    def __init__(self):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        self.first_name_fild = s('#firstName')
        self.last_name_fild = s('#lastName')
        self.email_fild = s('#userEmail')
        self.phone_fild = s('#userNumber')
        self.upload_picture_fild = s('#uploadPicture')
        self.address_fild = s('#currentAddress')
        self.state_fild = s('#react-select-3-input')
        self.city_fild = s('#react-select-4-input')
        self.submit_element = s('#submit')
        self.subjects_fild = s('#subjectsInput')
        self.gender_filds = ss('#genterWrapper label')
        self.hobbies_filds = ss('#hobbiesWrapper label')
        self.date_of_birth_fild = s('#dateOfBirthInput')

    def open(self):
        browser.open(self.base_url)

    def set_name(self, first_name, last_name):
        self.first_name_fild.set_value(first_name)
        self.last_name_fild.set_value(last_name)

    def set_email(self, email):
        self.email_fild.set_value(email)

    def set_phone(self, phone):
        self.phone_fild.set_value(phone)

    def set_picture(self, picture_name):
        self.upload_picture_fild.set_value(path_to_file(picture_name))

    def set_address(self, address):
        self.address_fild.set_value(address)

    def set_location(self, state, city):
        self.state_fild.set_value(state)
        self.city_fild.set_value(city)

    def submit(self):
        self.submit_element.press_enter()

    def set_subjects(self, subjects):
        for subject in subjects:
            self.subjects_fild.type(subject).press_enter()

    def choose_gender(self, gender):
        self.gender_filds.element_by(have.text(gender)).click()

    def choose_hobbies(self, hobbies):
        for hobbi in hobbies:
            self.hobbies_filds.element_by(have.text(hobbi)).click()



def choose_date_of_birth(day, month, year):
    s('#dateOfBirthInput').click()
    ss('.react-datepicker__month-select>option').element_by(have.text(month)).click()
    s(f'.react-datepicker__year-select').send_keys(year)
    s(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()





def check_submit_data(test_data):
    ss('.table').all('td').even.should(have.exact_texts(test_data))
