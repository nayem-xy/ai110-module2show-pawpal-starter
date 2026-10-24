
from diagrams.pawpal_system import Task, Pet


def test_task_completion():
    task = Task("Morning walk", "8:00 AM", "Daily")

    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_task_addition():
    pet = Pet("Buddy", "Dog")
    initial_count = len(pet.tasks)

    pet.add_task(Task("Breakfast", "8:30 AM", "Daily"))

    assert len(pet.tasks) == initial_count + 1
