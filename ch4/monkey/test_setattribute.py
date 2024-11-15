import pytest

# A simple class with an attribute we want to set


class MyClass:
    def __init__(self):
        self._value = None

# Custom function to mock the behavior of setting an attribute


def custom_setattr(self, name, value):
    print(f"Setting attribute '{name}' to '{
          value}' on {self.__class__.__name__}")
    object.__setattr__(self, name, value)  # Calls the original __setattr__

# Test function using monkeypatch to change the behavior of __setattr__


def test_monkeypatch_setattr(monkeypatch):
    # Create an instance of MyClass
    obj = MyClass()

    # Monkeypatch the __setattr__ method of the MyClass instance
    monkeypatch.setattr(obj, "__setattr__", custom_setattr)

    # Use the custom_setattr method to set an attribute
    obj.new_attr = 42  # This will use the custom __setattr__

    # Verify that the attribute is set correctly
    assert obj.new_attr == 42
