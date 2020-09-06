import pytest
from page_objects import problem_page
from problem_func import sock_merchant


def convert_test_data(sample_data):
    test_l = []
    for s_input, s_output in sample_data:
        n, line = s_input.split('\n')
        ar = list(map(int, line.split()))
        test_l.append([n, ar, int(s_output)])
    return test_l


page = problem_page.ProblemPage('sock-merchant')
test_data = convert_test_data(page.get_sample_data())


@pytest.mark.parametrize('n,ar,expected', test_data)
def test_sock_merchant(n, ar, expected):
    assert sock_merchant.sock_merchant(n, ar) == expected
