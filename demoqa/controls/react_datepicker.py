from selene import have
from selene.support.shared.jquery_style import ss, s


def set_date(selector, day, month, year):
    s(selector).click()
    ss('.react-datepicker__month-select>option').element_by(have.text(month)).click()
    s(f'.react-datepicker__year-select').send_keys(year)
    s(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
