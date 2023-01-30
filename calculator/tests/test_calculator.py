from src.basic_calculator import multiply, addition

def test_multiplication():
    assert multiply(2,2) == 4

def test_addition():
    assert addition(5,4) == 9
