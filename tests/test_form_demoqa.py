import os

from selene import be, have
from selene.support.shared import browser


def test_input_name():
    browser.element('#firstName').should(be.blank).type('Dart')
    browser.element('#firstName').should(have.value('Dart'))

    browser.element('#lastName').should(be.blank).type('Weider')
    browser.element('#lastName').should(have.value('Weider'))


def test_input_email():
    browser.element('#userEmail').should(be.blank).type('dartic-martic@starwars.com')
    browser.element('#userEmail').should(have.value('dartic-martic@starwars.com'))


def test_input_gender():
    browser.element('label[for=gender-radio-1]').click()


def test_input_phone():
    browser.element('#userNumber').should(be.blank).type('8005553555')
    browser.element('#userNumber').should(have.value('8005553555'))


def test_input_date_of_birth():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select>option[value="5"]').click()
    browser.element('.react-datepicker__year-select>option[value="2100"]').click()
    browser.element('.react-datepicker__day--030:not(.react-datepicker__day--outside-month)').click()
    browser.element('#dateOfBirthInput').should(have.value('30 Jun 2100'))


def test_subjects_input():
    subjects_list = 'Arts', 'Maths', 'Computer Science'
    for subject in subjects_list:
        browser.element('#subjectsInput').type(subject).press_enter()
    browser.all('.subjects-auto-complete__value-container .subjects-auto-complete__multi-value__label').should(
        have.exact_texts(subjects_list))


def test_hobbies_check_box():
    browser.element('label[for=hobbies-checkbox-3]').click()


def test_upload_picture():
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'media/123.jpeg'))
    )


def test_input_current_address():
    browser.element('#currentAddress').type('7th planet, 2d star of 234th galaxy')
    browser.element('#currentAddress').should(have.value('7th planet, 2d star of 234th galaxy'))


def test_city_input():
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()


def test_submit_button():
    browser.element('#submit').click()


def test_review_results():
    review_list = [
        'Student Name Dart Weider',
        'Student Email dartic-martic@starwars.com',
        'Gender Male',
        'Mobile 8005553555',
        'Date of Birth 30 June,2100',
        'Subjects Arts, Maths, Computer Science',
        'Hobbies Music',
        'Picture 123.jpeg',
        'Address 7th planet, 2d star of 234th galaxy',
        'State and City NCR Delhi'
    ]
    browser.all('.modal-body tbody tr').should(have.exact_texts(review_list))
    browser.element('#closeLargeModal').click()
