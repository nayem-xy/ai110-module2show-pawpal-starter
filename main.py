
from diagrams.pawpal_system import Task, Pet
from diagrams.pawpal_system import Task, Pet, Owner, Scheduler


def main():
    # Create tasks for each pet
    dog_tasks = [
        Task("Morning walk", "8:00 AM", "Daily"),
        Task("Breakfast", "8:30 AM", "Daily"),
    ]

    cat_tasks = [
        Task("Feed the cat", "9:00 AM", "Daily"),
        Task("Play with the cat", "6:00 PM", "Daily"),
    ]

    # Create at least two pets
    dog = Pet(name="Buddy", species="Dog", tasks=dog_tasks)
    cat = Pet(name="Luna", species="Cat", tasks=cat_tasks)

    # Create an owner with both pets
    owner = Owner(name="Nayem", pets=[dog, cat])

    # Create the scheduler
    scheduler = Scheduler(owner)

    # Retrieve tasks across all pets
    tasks = scheduler.get_tasks()

    # Print today's schedule
    print("Today's Schedule")
    print("================")

    for task in sorted(tasks, key=lambda t: t.time):
        status = "Completed" if task.completed else "Pending"
        print(
            f"{task.time} - {task.description} "
            f"({task.frequency}) [{status}]"
        )


if __name__ == "__main__":
    main()


def test_task_completion():
    task = Task("Morning walk", "8:00 AM", "Daily")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True
    print("PASS: Task completion works!")


def test_task_addition():
    pet = Pet("Buddy", "Dog")

    initial_count = pet.get_task_count()

    pet.add_task(Task("Breakfast", "8:30 AM", "Daily"))

    assert pet.get_task_count() == initial_count + 1
    print("PASS: Adding a task increases the task count!")


if __name__ == "__main__":
    test_task_completion()
    test_task_addition()
    print("All tests passed!")
