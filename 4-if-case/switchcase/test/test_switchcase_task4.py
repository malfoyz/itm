import pytest

from switchcase.task4 import execute_command


@pytest.mark.parametrize('initial_direction,command,expected_result',
                         [('С', 1, 'В'),
                          ('С', -1, 'З'),
                          ('Ю', -1, 'В'),
                          ('В', 1, 'Ю')])
def test_execute_command(initial_direction, command, expected_result):
    assert execute_command(initial_direction, command) == expected_result
