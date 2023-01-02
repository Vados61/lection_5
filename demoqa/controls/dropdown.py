from selene import command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

states = {
    'NCR': 0,
    'Uttar Pradesh': 1,
    'Haryana': 2,
    'Rajasthan': 3
}
cities = {
    'Delhi': 0,
    'Gurgaon': 1,
    'Noida': 2
}


def select_location(state, city):
    s('#state').perform(command.js.scroll_into_view).click()
    s(f'#react-select-3-option-{states[state]}').click()
    s('#city').click()
    s(f'#react-select-4-option-{cities[city]}').click()
