
from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True


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


class Scheduler:
    def __init__(self, owner: Owner):
        """Initialize the scheduler with an owner."""
        self.owner = owner

    def get_tasks(self) -> List[Task]:
        """Retrieve all tasks through the owner."""
        return self.owner.get_all_tasks()

    def organize_tasks(self) -> List[Task]:
        """Return all tasks for scheduling."""
        tasks = self.get_tasks()
        return tasks
