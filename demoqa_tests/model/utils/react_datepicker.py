import datetime

from selene import have
from selene.support.shared.jquery_style import s, ss

from demoqa_tests.model.utils import config


def set_date(selector, date: datetime.date):
    day, month, year = date.strftime(config.datetime_input_format).split()
    s(selector).click()
    ss('.react-datepicker__month-select>option').element_by(have.text(month)).click()
    s(f'.react-datepicker__year-select').send_keys(year)
    s(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
