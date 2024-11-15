import os
import pytest

# Example function that depends on an environment variable


def get_env_variable():
    return os.getenv("MY_ENV_VAR", "default_value")

# Test function using monkeypatch.setenv to set environment variable


def test_setenv(monkeypatch):
    # Print the initial environment variable (this will return None or the default)
    print(f"Initial MY_ENV_VAR: {get_env_variable()}")

    # Set the environment variable 'MY_ENV_VAR' to 'test_value' using monkeypatch
    monkeypatch.setenv("MY_ENV_VAR", "test_value")

    # Now when we call the function, it should return 'test_value'
    print(f"Modified MY_ENV_VAR: {get_env_variable()}")

    # Assertions to verify the environment variable is set correctly
    assert get_env_variable() == "test_value"

    # Test the case when an environment variable is not set (it should fallback to default)
    # Remove the environment variable
    monkeypatch.delenv("MY_ENV_VAR", raising=False)
    assert get_env_variable() == "default_value"
