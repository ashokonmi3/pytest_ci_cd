import pytest

# Parameterized fixture example
@pytest.fixture(params=[("apple", 1), ("banana", 2), ("cherry", 3)])
def fruit_data(request):
    # request.param will hold each value in params in each test invocation
    return request.param


def test_fruit_quantity(fruit_data):
    fruit, quantity = fruit_data
    print(f"Testing fruit: {fruit} with quantity: {quantity}")
    assert quantity > 0
