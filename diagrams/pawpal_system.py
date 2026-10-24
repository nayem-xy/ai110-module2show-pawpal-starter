
from dataclasses import dataclass, field
from typing import List, Dict, Optional


# 1. Pet: Stores information about a pet and its care needs
@dataclass
class Pet:
    pet_id: int
    name: str
    species: str
    age: int
    care_requirements: List[str] = field(default_factory=list)

    def get_care_requirements(self) -> List[str]:
        pass

    def update_care_requirements(self, requirements: List[str]) -> None:
        pass


# 2. CareTask: Represents an individual pet care activity
@dataclass
class CareTask:
    task_id: int
    task_name: str
    duration: int
    priority: int
    frequency: str
    due_time: Optional[str] = None
    task_type: str = "general"

    def is_due(self) -> bool:
        pass

    def calculate_priority(self) -> int:
        pass

    def mark_completed(self) -> None:
        pass


# 3. Owner: Stores the owner's schedule and preferences
@dataclass
class Owner:
    owner_id: int
    available_time: int
    preferences: List[str] = field(default_factory=list)
    schedule: Dict[str, List[str]] = field(default_factory=dict)
    pets: List[Pet] = field(default_factory=list)

    def get_available_time(self) -> int:
        pass

    def update_preferences(self, preferences: List[str]) -> None:
        pass

    def check_availability(self, required_time: int) -> bool:
        pass


# 4. DailyPlanner: Generates and explains a daily pet care plan
@dataclass
class DailyPlanner:
    plan_date: str
    tasks: List[CareTask] = field(default_factory=list)
    total_duration: int = 0
    reasoning: str = ""

    def generate_plan(self, owner: Owner, pet: Pet) -> List[CareTask]:
        pass

    def prioritize_tasks(self, tasks: List[CareTask]) -> List[CareTask]:
        pass

    def check_time_constraints(self, owner: Owner) -> bool:
        pass

    def explain_plan(self) -> str:
        pass
