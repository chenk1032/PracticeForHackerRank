import pytest
from page_objects import problem_page
from problem_func import migratory_birds


def convert_test_data(sample_data):
    test_l = []
    for s_input, s_output in sample_data:
        i = list(map(int, s_input.split('\n')[1].split()))
        test_l.append([i, int(s_output)])
    return test_l


page = problem_page.ProblemPage('migratory-birds')
test_data = convert_test_data(page.get_sample_data())


@pytest.mark.parametrize('arr,expected', test_data)
def test_migratory_birds(arr, expected):
    assert migratory_birds.migratory_birds(arr) == expected
