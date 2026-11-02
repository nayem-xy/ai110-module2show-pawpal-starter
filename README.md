# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:
Pet Owner: Jordan

Registered Pets:
- Mochi — Dog
- Luna — Cat

Daily Schedule:

08:00 AM — Morning walk
Pet: Mochi
Frequency: Daily
Status: Pending

09:00 AM — Feeding
Pet: Luna
Frequency: Daily
Status: Pending

06:00 PM — Dinner
Pet: Mochi
Frequency: Daily
Status: Pending

Showing 3 task(s) across 2 pet(s)

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```
test_pawpal_system.py::test_task_completion PASSED
test_pawpal_system.py::test_task_addition PASSED

========================= 2 passed =========================


## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step --> Launch the application using python3 -m streamlit run app.py.
2. <!-- Describe this step --> Enter or update the pet owner's name.
3. <!-- Describe this step --> Add pets by providing their names and species. The application stores them through the Owner.add_pet() method.
4. <!-- Describe this step -->Select a pet and create care tasks by entering a description, scheduled time, and frequency. The tasks are added through the Pet.add_task() method.
5. <!-- Add more steps as needed --> Click Generate schedule to retrieve tasks across all pets through the Scheduler and display them in chronological order.
6.Click Mark as complete beside a pending task to update its completion status.
7.Review the updated schedule and completion status.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->

Implementation Summary

PawPal+ is a pet care scheduling application built with Python and Streamlit. It uses four main classes:

Task: Represents a care activity with a description, scheduled time, frequency, and completion status. Its mark_complete() method updates the task's status.

Pet: Stores pet information and its assigned tasks. Its add_task() method adds tasks, while get_task_count() returns the number of assigned tasks.

Owner: Stores the owner's information and manages multiple pets. Its add_pet() method adds a pet, and get_all_tasks() collects tasks across all pets.

Scheduler: Uses the Owner object to retrieve all tasks and organize them chronologically.

The Streamlit interface connects the backend classes to interactive forms and buttons. Streamlit's session state preserves the Owner object and associated pet and task data across normal app reruns.