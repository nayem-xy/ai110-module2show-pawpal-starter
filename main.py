
from datetime import date

from diagrams.pawpal_system import Task, Pet, Owner, Scheduler


def main():
    # Create tasks in a deliberately mixed-up order.
    dog_tasks = [
        Task("Dinner", "6:00 PM", "Daily"),
        Task("Morning walk", "8:00 AM", "Daily"),
        Task("Vet appointment", "10:00 AM", "Once"),
    ]

    cat_tasks = [
        Task("Play with the cat", "6:00 PM", "Daily"),
        Task("Breakfast", "9:00 AM", "Daily"),
    ]

    # Create two pets.
    dog = Pet(name="Buddy", species="Dog", tasks=dog_tasks)
    cat = Pet(name="Luna", species="Cat", tasks=cat_tasks)

    # Create the owner and scheduler.
    owner = Owner(name="Nayem", pets=[dog, cat])
    scheduler = Scheduler(owner)

    # 1. Display tasks in chronological order.
    print("\nTODAY'S SCHEDULE")
    print("================")

    for task in scheduler.sort_by_time():
        status = "Completed" if task.completed else "Pending"
        print(
            f"{task.time} - {task.description} "
            f"({task.frequency}) [{status}]"
        )

    # 2. Display only Buddy's tasks.
    print("\nBUDDY'S TASKS")
    print("=============")

    for task in scheduler.filter_by_pet("Buddy"):
        print(f"{task.time} - {task.description}")

    # 3. Display pending tasks.
    print("\nPENDING TASKS")
    print("============")

    for task in scheduler.filter_by_status(completed=False):
        print(f"{task.time} - {task.description}")

    # 4. Complete a daily task and check its next occurrence.
    print("\nRECURRING TASK")
    print("==============")

    morning_walk = dog.tasks[1]
    next_task = scheduler.complete_task(morning_walk)

    print(f"Completed: {morning_walk.description}")

    if next_task:
        print(
            f"Next occurrence: {next_task.due_date} "
            f"at {next_task.time}"
        )

    # 5. Check for scheduling conflicts.
    print("\nSCHEDULING CONFLICTS")
    print("====================")

    conflicts = scheduler.detect_conflicts()

    if conflicts:
        for warning in conflicts:
            print(f"WARNING: {warning}")
    else:
        print("No scheduling conflicts found.")

    # 6. Show the total number of tasks.
    print("\nTOTAL TASKS")
    print("===========")
    print(f"Owner: {owner.name}")
    print(f"Pets: {len(owner.pets)}")
    print(f"Tasks: {len(scheduler.get_tasks())}")


if __name__ == "__main__":
    main()
