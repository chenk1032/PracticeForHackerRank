import pytest
from page_objects import problem_page
from problem_func import day_of_programmer


def convert_test_data(sample_data):
    return [[int(s_input), s_output] for s_input, s_output in sample_data]


page = problem_page.ProblemPage('day-of-the-programmer')
test_data = convert_test_data(page.get_sample_data())


@pytest.mark.parametrize('year,expected', test_data)
def test_day_of_programmer(year, expected):
    assert day_of_programmer.day_of_programmer(year) == expected
