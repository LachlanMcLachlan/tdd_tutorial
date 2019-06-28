from tdd_tutorial.useful_functions.my_functions import say_hello

def test_print_hello():
    expected_output = 'Hello'
    true_output = say_hello()
    assert expected_output == true_output