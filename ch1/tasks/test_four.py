"""Test the Task data type."""
import pytest
from collections import namedtuple
import time

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    # time.sleep(2)
    assert t_dict == expected


@pytest.mark.smoke
def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 11)
    # time.sleep(3)

    assert t_after == t_expected


# Test File Name
# test_ < something > .py or <something > _test.py


# Test name
# test_ < something > .py

# Class name
# Test < something >
