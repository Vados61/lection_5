from selene import have
from selene.support.shared.jquery_style import ss


def get_element(name, value):
    return ss(f'[name={name}').element_by(have.value(value)).element('..')
