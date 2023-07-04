import pytest

from HW_14.human import Human


def test_name_private(create_human):
    """Test name is private"""
    human = create_human
    with pytest.raises(AttributeError, match=f"'{human.__class__.__name__}' object has no attribute '__name'"):
        assert 'Sam' == human.__name


def test_status_private(create_human):
    """Test status is private"""
    human = create_human
    with pytest.raises(AttributeError, match=f"'{human.__class__.__name__}' object has no attribute '__status'"):
        assert 'alive' == human.__status


def test_age_limit_private(create_human):
    """Test age_limit is private"""
    human = create_human
    with pytest.raises(AttributeError, match=f"'{human.__class__.__name__}' object has no attribute '__age_limit'"):
        assert '100' == human.__age_limit


def test_age_property(create_human):
    """Test age property"""
    human = create_human
    assert 18 == human.age


def test_gender_property(create_human):
    """Test gender property"""
    human = create_human
    assert 'male' == human.gender


def test_human_grow(create_human):
    """Test valid grow of a human"""
    human = create_human
    new_age = human.age + 1
    human.grow()
    assert new_age == human.age


def test_human_is_dead(create_diff_human):
    """
    1. Test that grow is not possible above age limit
    2. Test private function __is_alive
    """
    name = 'Pam'
    old_human = create_diff_human(name, 100, 'female')
    old_human.grow()
    with pytest.raises(Exception, match=f'{name} is already dead...'):
        old_human.grow()


def test_change_valid_gender(create_human):
    """Test valid change of human's gender"""
    male_human = create_human
    new_gender = 'female'
    male_human.change_gender('female')
    assert new_gender == male_human.gender


def test_change_to_current_gender(create_diff_human):
    """Test not possible change of gender to current one"""
    name = 'Sam'
    male_human = create_diff_human(name, 100, 'male')
    new_gender = 'male'
    with pytest.raises(Exception, match=f"{name} already has gender '{new_gender}'"):
        male_human.change_gender(new_gender)


def test_change_to_non_existing_gender(create_human):
    """Test changing gender to non-existing one"""
    human = create_human
    new_gender = 'trans woman'
    with pytest.raises(Exception, match="Not correct name of gender"):
        human.change_gender(new_gender)


def test_change_gender_of_dead(create_diff_human):
    """Test change gender of dead human"""
    human_name = 'Bonny'
    dead_human = create_diff_human(human_name, 100, 'female')
    dead_human.grow()
    with pytest.raises(Exception, match=f"{human_name} is already dead..."):
        dead_human.change_gender('male')


def test_is_alive_private(create_human):
    """Test is_alive method is private"""
    human = create_human
    with pytest.raises(AttributeError, match=f"'{human.__class__.__name__}' object has no attribute '__is_alive'"):
        human.__is_alive()


def test_validate_gender_private():
    """Test validate_gender method is private"""
    with pytest.raises(AttributeError, match=f"type object 'Human' has no attribute '__validate_gender'"):
        assert Human.__validate_gender()
