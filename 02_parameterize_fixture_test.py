import pytest

# Simulate Task class

class Task:
    def __init__(self, summary, owner=None, done=False):
        self.summary = summary
        self.owner = owner
        self.done = done

    def __repr__(self):
        return f"Task(summary='{self.summary}', owner='{self.owner}', done={self.done})"


# Sample tasks for parameterization
tasks_to_try = [
    Task("sleep", done=True),
    Task("wake", "brian"),
    Task("breathe", "BRIAN", True),
    Task("exercise", "BrIaN", False),
]

# Task ids formatted for readability
task_ids = ["Task({},{},{})".format(t.summary, t.owner, t.done)
            for t in tasks_to_try] # Task(sleep,True,False)


# Simulate in-memory task database
class InMemoryTasksDB:
    def __init__(self):
        self._tasks = {}
        self._current_id = 1
        print("\n[DB] Initialized in-memory database")

    def add(self, task):
        task_id = self._current_id
        self._tasks[task_id] = task
        self._current_id += 1
        print(f"[DB] Added {task} with ID {task_id}")
        return task_id

    def get(self, task_id):
        task = self._tasks.get(task_id)
        print(f"[DB] Retrieved {task} with ID {task_id}")
        return task

    def delete_all(self):
        self._tasks.clear()
        self._current_id = 1
        print("[DB] Cleared all tasks")


# Function to check if two tasks are equivalent
def equivalent(t1, t2):
    """Check two tasks for equivalence."""
    return (
        (t1.summary == t2.summary) and
        (t1.owner == t2.owner) and
        (t1.done == t2.done)
    )


# Fixtures for task database
@pytest.fixture(scope="session")
def tasks_db_session():
    """Set up the in-memory database before tests and clean up after."""
    print("\n[Fixture] Setting up session-level tasks_db_session")
    db = InMemoryTasksDB()
    yield db
    print("[Fixture] Tearing down session-level tasks_db_session")
    db.delete_all()


@pytest.fixture()
def tasks_db(tasks_db_session):
    """Ensure an empty tasks db for each test."""
    print("\n[Fixture] Setting up function-level tasks_db")
    tasks_db_session.delete_all()
    return tasks_db_session


# Parameterized fixtures

# Fixture for tasks without ids
@pytest.fixture(params=tasks_to_try)
def a_task(request):
    """Using no ids."""
    task = request.param
    print(f"\n[Fixture] Providing parameterized task: {task}")
    return task


# Fixture for tasks with ids
@pytest.fixture(params=tasks_to_try, ids=task_ids)
def b_task(request):
    """Using a list of ids."""
    task = request.param
    print(f"\n[Fixture] Providing parameterized task with id: {task}")
    return task


# Custom function to generate task ids
def id_func(fixture_value):
    """A function for generating ids."""
    t = fixture_value
    return "Task({},{},{})".format(t.summary, t.owner, t.done)


# Fixture using a custom id function
@pytest.fixture(params=tasks_to_try, ids=id_func)
def c_task(request):
    """Using a function (id_func) to generate ids."""
    task = request.param
    print(
        f"\n[Fixture] Providing parameterized task with generated id: {task}")
    return task


# Test functions

def test_add_a(tasks_db, a_task):
    """Using a_task fixture (no ids)."""
    print(f"\n[Test] Running test_add_a with task: {a_task}")
    task_id = tasks_db.add(a_task)
    t_from_db = tasks_db.get(task_id)
    assert equivalent(t_from_db, a_task)
    print("[Test] Test passed")


def test_add_b(tasks_db, b_task):
    """Using b_task fixture, with ids."""
    print(f"\n[Test] Running test_add_b with task: {b_task}")
    task_id = tasks_db.add(b_task)
    t_from_db = tasks_db.get(task_id)
    assert equivalent(t_from_db, b_task)
    print("[Test] Test passed")


def test_add_c(tasks_db, c_task):
    """Use fixture with generated ids."""
    print(f"\n[Test] Running test_add_c with task: {c_task}")
    task_id = tasks_db.add(c_task)
    t_from_db = tasks_db.get(task_id)
    assert equivalent(t_from_db, c_task)
    print("[Test] Test passed")
