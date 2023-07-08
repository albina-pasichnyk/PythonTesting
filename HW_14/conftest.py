import pytest

from HW_14.human import Human

import random


@pytest.fixture(scope='session', autouse=True)
def create_human():
    ages = random.randint(1, 99)
    human = Human('Sam', ages, 'male')
    yield human


@pytest.fixture()
def create_custom_human():
    def __create_human(name, age, gender):
        human = Human(name=name, age=age, gender=gender)
        return human

    return __create_human


@pytest.fixture()
def create_human_with_age():
    def __create_human(age):
        human = Human(name='Same', age=age, gender='male')
        return human

    return __create_human


@pytest.fixture()
def create_human_with_gender():
    def __create_human(gender):
        human = Human(name='Sam', age=18, gender=gender)
        return human

    return __create_human
