import pytest

from HW_14.human import Human


@pytest.fixture(scope='session', autouse=True)
def create_human():
    human = Human('Sam', 18, 'male')
    yield human


@pytest.fixture()
def create_diff_human():
    def __create_human(name, age, gender):
        human = Human(name=name, age=age, gender=gender)
        return human

    return __create_human
