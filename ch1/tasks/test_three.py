"""Test the Task data type."""
import time
import pytest
from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """Using no parameters should invoke defaults."""
    print("Executing the test_defaults ")
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2
    # time.sleep(4)

    print("[Finished] Executing the test_defaults ")


@pytest.mark.smoke
def test_member_access():
    """Check .field functionality of namedtuple."""
    print("Executing the test_member_access ")

    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)
    # time.sleep(5)

    print("[Finished] Executing the test_member_access ")
