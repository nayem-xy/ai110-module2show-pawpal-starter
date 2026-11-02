from datetime import date, timedelta

from diagrams.pawpal_system import Task, Pet, Owner, Scheduler


def create_scheduler():
    """Create sample pets and tasks for testing."""
    dog = Pet(
        "Buddy",
        "Dog",
        [
            Task("Morning walk", "8:00 AM", "Daily"),
            Task("Dinner", "6:00 PM", "Daily"),
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


def test_sorting_correctness():
    scheduler, dog, cat = create_scheduler()

    sorted_tasks = scheduler.sort_by_time()

    assert [task.time for task in sorted_tasks] == [
        "8:00 AM",
        "9:00 AM",
        "6:00 PM",
    ]


def test_daily_recurring_task():
    scheduler, dog, cat = create_scheduler()

    task = dog.tasks[0]
    next_task = scheduler.complete_task(task)

    assert task.completed is True
    assert next_task is not None
    assert next_task.due_date == date.today() + timedelta(days=1)
    assert next_task.description == task.description
    assert next_task.completed is False


def test_conflict_detection():
    scheduler, dog, cat = create_scheduler()

    cat.add_task(Task("Evening feeding", "6:00 PM", "Daily"))

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "6:00 PM" in conflicts[0]


def test_different_dates_are_not_conflicts():
    scheduler, dog, cat = create_scheduler()

    tomorrow = date.today() + timedelta(days=1)

    cat.add_task(
        Task(
            "Evening feeding",
            "6:00 PM",
            "Once",
            due_date=tomorrow,
        )
    )

    assert scheduler.detect_conflicts() == []


def test_empty_schedule():
    pet = Pet("Buddy", "Dog")
    owner = Owner("Nayem", [pet])
    scheduler = Scheduler(owner)

    assert scheduler.get_tasks() == []
    assert scheduler.sort_by_time() == []
    assert scheduler.detect_conflicts() == []
