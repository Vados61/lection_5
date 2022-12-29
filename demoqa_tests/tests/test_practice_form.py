from datetime import date

import allure
from allure_commons.types import Severity

from demoqa_tests.model.pages import practise_form
from demoqa_tests.model.user import Student


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Vados61')
@allure.feature('Проверка правильности заполнения формы студента')
@allure.link('https://demoqa.com/automation-practice-form', name='Practise-form')
def test_filling_form():
    form_page = practise_form.Page()
    student = Student(
        first_name='Dart',
        last_name='Weider',
        email='dartic-martic@starwars.com',
        gender='Male',
        phone_number=8005553555,
        image='123.jpeg',
        subjects=('Arts', 'Maths', 'Computer Science'),
        hobbies=('Reading', 'Music'),
        address='7th planet, 2d star of 234th galaxy',
        state='NCR',
        city='Delhi',
        date_of_birth=date(2100, 3, 15)
    )
    with allure.step('Открываем страницу заполнения формы'):
        form_page.open()

    with allure.step('Заполняем имя и фамилию'):
        form_page.set_name(first_name=student.first_name, last_name=student.last_name)
    with allure.step('Заполняем почту'):
        form_page.set_email(student.email)
    with allure.step('Выбираем пол'):
        form_page.set_gender(student.gender)
    with allure.step('Заполняем телефон'):
        form_page.set_phone(student.phone_number)
    with allure.step('Выбираем предметы'):
        form_page.set_subjects(student.subjects)
    with allure.step('Выбираем хобби'):
        form_page.set_hobbies(student.hobbies)
    with allure.step('Выбираем фото из папки media'):
        form_page.set_picture(student.image)
    with allure.step('Заполняем адрес'):
        form_page.set_address(student.address)
    with allure.step('Выставляем дату рождения'):
        form_page.set_date_of_birth(student.date_of_birth)
    with allure.step('Выбираем штат и город'):
        form_page.set_location(state=student.state, city=student.city)

    with allure.step('Сличаем данные из формы с исходными'):
        form_page.check_submit_data(student)










