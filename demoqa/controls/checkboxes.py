from selene import have
from selene.support.shared.jquery_style import ss, s

hobbies = {
    "Sports": "1",
    "Reading": "2",
    "Music": "3"
}


def select_items(items):
    for item in items:
        ss(f"input[type='checkbox']").element_by(have.value(hobbies[item])).s('..').click()
