
#Ejidia, Patience and Linda
def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be non-negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def test_fibonacci_zero():
    assert fibonacci(0) == 0

def test_fibonacci_one():
    assert fibonacci(1) == 1

def test_fibonacci_two():
    assert fibonacci(2) == 1

def test_fibonacci_five():
    assert fibonacci(5) == 5

def test_fibonacci_ten():
    assert fibonacci(10) == 55

def test_fibonacci_negative():
    try:
        fibonacci(-1)
        assert False  # Fail the test if no error is raised
    except ValueError:
        assert True  # Pass if ValueError is raised