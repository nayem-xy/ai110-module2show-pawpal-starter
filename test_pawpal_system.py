
from datetime import date, timedelta

from diagrams.pawpal_system import Task, Pet, Owner, Scheduler


def create_scheduler():
    """Create a sample owner and scheduler for testing."""
    dog = Pet(
        "Buddy",
        "Dog",
        [
            Task("Dinner", "6:00 PM", "Daily"),
            Task("Walk", "8:00 AM", "Daily"),
        ],
    )

    cat = Pet(
        "Luna",
        "Cat",
        [
            Task("Breakfast", "9:00 AM", "Daily"),
        ],
    )

    owner = Owner("Nayem", [dog, cat])
    return Scheduler(owner), dog, cat


def test_task_completion():
    task = Task("Morning walk", "8:00 AM", "Daily")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_task_addition():
    pet = Pet("Buddy", "Dog")

    initial_count = pet.get_task_count()
    pet.add_task(Task("Breakfast", "8:30 AM", "Daily"))

    assert pet.get_task_count() == initial_count + 1


def test_sort_by_time():
    scheduler, dog, cat = create_scheduler()

    sorted_tasks = scheduler.sort_by_time()

    assert [task.time for task in sorted_tasks] == [
        "8:00 AM",
        "9:00 AM",
        "6:00 PM",
    ]


def test_filter_by_status():
    scheduler, dog, cat = create_scheduler()

    dog.tasks[1].mark_complete()

    pending_tasks = scheduler.filter_by_status(completed=False)
    completed_tasks = scheduler.filter_by_status(completed=True)

    assert len(pending_tasks) == 2
    assert len(completed_tasks) == 1


def test_filter_by_pet():
    scheduler, dog, cat = create_scheduler()

    cat_tasks = scheduler.filter_by_pet("luna")

    assert len(cat_tasks) == 1
    assert cat_tasks[0].description == "Breakfast"


def test_daily_recurring_task():
    scheduler, dog, cat = create_scheduler()

    task = dog.tasks[1]
    next_task = scheduler.complete_task(task)

    assert task.completed is True
    assert next_task is not None
    assert next_task.due_date == date.today() + timedelta(days=1)
    assert next_task.description == task.description
    assert next_task.completed is False


def test_weekly_recurring_task():
    scheduler, dog, cat = create_scheduler()

    weekly_task = Task("Grooming", "11:00 AM", "Weekly")
    dog.add_task(weekly_task)

    next_task = scheduler.complete_task(weekly_task)

    assert next_task is not None
    assert next_task.due_date == date.today() + timedelta(weeks=1)


def test_once_task_does_not_repeat():
    scheduler, dog, cat = create_scheduler()

    once_task = Task("Vet appointment", "10:00 AM", "Once")
    dog.add_task(once_task)

    next_task = scheduler.complete_task(once_task)

    assert once_task.completed is True
    assert next_task is None


def test_conflict_detection():
    scheduler, dog, cat = create_scheduler()

    # Add a task for Luna at the same time as Buddy's dinner.
    cat.add_task(Task("Evening feeding", "6:00 PM", "Daily"))

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "6:00 PM" in conflicts[0]


def test_completed_tasks_are_not_reported_as_conflicts():
    scheduler, dog, cat = create_scheduler()

    dog.tasks[0].mark_complete()
    cat.add_task(Task("Evening feeding", "6:00 PM", "Daily"))

    conflicts = scheduler.detect_conflicts()

    assert conflicts == []
