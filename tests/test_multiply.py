def multiply(a, b):
    return a * b

def test_multiply_1_by_1():
    assert multiply(1, 1) == 1  

    def test_multiply_2_by_2():
        assert multiply(2, 2) == 4
        