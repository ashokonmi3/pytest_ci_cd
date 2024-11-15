"""Define some fixtures to use in the project."""

import pytest
import tasks
from tasks import Task


@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after."""
    # Setup : start db
    print("\n Connect to db before tests")
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()
    print("\n Disconnect to db after tests")


# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# summary is required
# owner and done are optional
# id is set by database


@pytest.fixture()
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task("Write some code", "Brian", True),
        Task("Code review Brian's code", "Katie", False),
        Task("Fix what Brian did", "Michelle", False),
    )


@pytest.fixture()
def tasks_mult_per_owner():
    """Several owners with several tasks each."""
    return (
        Task("Make a cookie", "Raphael"),
        Task("Use an emoji", "Raphael"),
        Task("Move to Berlin", "Raphael"),
        Task("Create", "Michelle"),
        Task("Inspire", "Michelle"),
        Task("Encourage", "Michelle"),
        Task("Do a handstand", "Daniel"),
        Task("Write some books", "Daniel"),
        Task("Eat ice cream", "Daniel"),
    )


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connected db with 3 tasks, all unique."""
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    """Connected db with 9 tasks, 3 owners, all with 3 tasks."""
    for t in tasks_mult_per_owner:
        tasks.add(t)
