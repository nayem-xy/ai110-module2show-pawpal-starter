
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from typing import List


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def next_occurrence(self):
        """Create the next task for a daily or weekly schedule."""
        if self.frequency.lower() == "daily":
            next_date = self.due_date + timedelta(days=1)
        elif self.frequency.lower() == "weekly":
            next_date = self.due_date + timedelta(weeks=1)
        else:
            return None

        return Task(
            description=self.description,
            time=self.time,
            frequency=self.frequency,
            due_date=next_date,
        )


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to the pet's task list."""
        self.tasks.append(task)

    def get_task_count(self) -> int:
        """Return the number of tasks assigned to the pet."""
        return len(self.tasks)


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks belonging to the owner's pets."""
        all_tasks = []

        for pet in self.pets:
            all_tasks.extend(pet.tasks)

        return all_tasks

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)


class Scheduler:
    def __init__(self, owner: Owner):
        """Initialize the scheduler with an owner."""
        self.owner = owner

    def get_tasks(self) -> List[Task]:
        """Retrieve all tasks through the owner."""
        return self.owner.get_all_tasks()

    def sort_by_time(self) -> List[Task]:
        """Sort tasks by due date and scheduled time."""
        return sorted(
            self.get_tasks(),
            key=lambda task: (
                task.due_date,
                datetime.strptime(task.time, "%I:%M %p"),
            ),
        )

    def organize_tasks(self) -> List[Task]:
        """Return all tasks in chronological order."""
        return self.sort_by_time()

    def filter_by_status(self, completed: bool) -> List[Task]:
        """Return tasks matching the requested completion status."""
        return [
            task for task in self.get_tasks()
            if task.completed == completed
        ]

    def filter_by_pet(self, pet_name: str) -> List[Task]:
        """Return tasks assigned to a pet by name."""
        matching_tasks = []

        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                matching_tasks.extend(pet.tasks)

        return matching_tasks

    def complete_task(self, task: Task):
        """Complete a task and add its next occurrence if recurring."""
        for pet in self.owner.pets:
            if task in pet.tasks:
                if task.completed:
                    return None

                task.mark_complete()
                next_task = task.next_occurrence()

                if next_task is not None:
                    pet.add_task(next_task)

                return next_task

        return None

    def detect_conflicts(self) -> List[str]:
        """Return warnings for tasks scheduled at the same time."""
        tasks_by_time = {}

        for pet in self.owner.pets:
            for task in pet.tasks:
                if task.completed:
                    continue

                # Convert the time to a consistent format for comparison.
                normalized_time = datetime.strptime(
                    task.time, "%I:%M %p"
                ).strftime("%I:%M %p")

                if normalized_time not in tasks_by_time:
                    tasks_by_time[normalized_time] = []

                tasks_by_time[normalized_time].append(
                    (pet.name, task.description)
                )

        warnings = []

        for scheduled_time, tasks in tasks_by_time.items():
            if len(tasks) > 1:
                task_details = ", ".join(
                    f"{description} ({pet_name})"
                    for pet_name, description in tasks
                )

                warnings.append(
                    f"Conflict at {scheduled_time}: {task_details}"
                )

        return warnings
