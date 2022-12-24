import allure
from allure_commons.types import Severity

from selene.support.shared import browser
from demoqa import practise_form


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Vados61')
@allure.feature('Проверка правильности заполнения формы студента')
@allure.link('https://demoqa.com/automation-practice-form', name='Practise-form')
def test_practis_form():
    with allure.step('Открываем страницу заполнения формы'):
        browser.open('https://demoqa.com/automation-practice-form')

    with allure.step('Заполняем имя и фамилию'):
        practise_form.type_name('Dart')
        practise_form.type_last_name('Weider')

    with allure.step('Заполняем почту'):
        practise_form.type_email('dartic-martic@starwars.com')

    with allure.step('Выбираем пол'):
        practise_form.choose_gender('Male')

    with allure.step('Заполняем телефон'):
        practise_form.type_phone('8005553555')

    with allure.step('Выставляем дату рождения'):
        practise_form.choose_date_of_birth(day=15, month='May', year=2100)

    with allure.step('Выбираем предметы'):
        subjects_list = 'Arts', 'Maths', 'Computer Science'
        practise_form.choose_sabjects(subjects_list)

    with allure.step('Выбираем хобби'):
        practise_form.choose_hobbies(['Reading', 'Music'])

    with allure.step('Выбираем фото из папки media'):
        practise_form.choose_photo('123.jpeg')

    with allure.step('Заполняем адрес'):
        practise_form.type_adress('7th planet, 2d star of 234th galaxy')

    with allure.step('Выбираем штат и город'):
        practise_form.choose_state_and_city(state='NCR', city='Delhi')

    with allure.step('Сличаем данные из формы с исходными'):
        test_data = [
            'Dart Weider',
            'dartic-martic@starwars.com',
            'Male', '8005553555',
            '15 May,2100',
            'Arts, Maths, Computer Science',
            'Reading, Music',
            '123.jpeg',
            '7th planet, 2d star of 234th galaxy',
            'NCR Delhi'
        ]
        practise_form.check_submit_data(test_data)
