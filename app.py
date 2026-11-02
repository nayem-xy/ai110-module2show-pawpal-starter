
import streamlit as st
from datetime import datetime

from diagrams.pawpal_system import Owner, Pet, Scheduler, Task


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered",
)

st.title("🐾 PawPal+")
st.write("Your personal assistant for managing pet care tasks.")


# --------------------------------------------------
# Initialize session state
# --------------------------------------------------

# Create the Owner only once per Streamlit session.
if "owner" not in st.session_state:
    st.session_state.owner = Owner(
        name="Jordan",
        pets=[Pet(name="Mochi", species="dog")],
    )

if "schedule_generated" not in st.session_state:
    st.session_state.schedule_generated = False

owner = st.session_state.owner
scheduler = Scheduler(owner)


# --------------------------------------------------
# Owner information
# --------------------------------------------------

st.subheader("Pet Owner")

owner.name = st.text_input(
    "Owner name",
    value=owner.name,
)


# --------------------------------------------------
# Add a pet
# --------------------------------------------------

st.divider()
st.subheader("Your Pets")

with st.expander("Add another pet"):
    with st.form("add_pet_form"):
        new_pet_name = st.text_input("Pet name")

        new_species = st.selectbox(
            "Species",
            ["Dog", "Cat", "Bird", "Other"],
        )

        add_pet_submitted = st.form_submit_button("Add Pet")

    if add_pet_submitted:
        cleaned_name = new_pet_name.strip()

        if cleaned_name:
            new_pet = Pet(
                name=cleaned_name,
                species=new_species.lower(),
            )

            # Add the new Pet object through the Owner class.
            owner.add_pet(new_pet)

            st.success(f"{new_pet.name} was added successfully!")
            st.rerun()

        else:
            st.warning("Please enter a pet name.")


# Display all registered pets.
st.markdown("### Registered Pets")

if owner.pets:
    for pet in owner.pets:
        st.write(f"🐾 **{pet.name}** — {pet.species.title()}")
else:
    st.info("No pets have been added yet.")


# --------------------------------------------------
# Select a pet
# --------------------------------------------------

if owner.pets:
    selected_pet_name = st.selectbox(
        "Select a pet to manage",
        options=[pet.name for pet in owner.pets],
    )

    selected_pet = next(
        pet for pet in owner.pets
        if pet.name == selected_pet_name
    )

    # --------------------------------------------------
    # Add a task
    # --------------------------------------------------

    st.divider()
    st.subheader(f"Schedule Care for {selected_pet.name}")

    with st.form("add_task_form"):
        description = st.text_input(
            "Task description",
            placeholder="Morning walk",
        )

        task_time = st.time_input("Scheduled time")

        frequency = st.selectbox(
            "Frequency",
            ["Once", "Daily", "Weekly"],
        )

        add_task_submitted = st.form_submit_button("Add task")

    if add_task_submitted:
        cleaned_description = description.strip()

        if not cleaned_description:
            st.error("Please enter a task description.")

        else:
            new_task = Task(
                description=cleaned_description,
                time=task_time.strftime("%I:%M %p"),
                frequency=frequency,
            )

            # Add the Task object through the Pet class.
            selected_pet.add_task(new_task)

            st.success(
                f"Task '{new_task.description}' added for "
                f"{selected_pet.name}!"
            )
            st.rerun()


# --------------------------------------------------
# Generate and display the schedule
# --------------------------------------------------

st.divider()
st.subheader("📅 Care Schedule")

if st.button("Generate schedule", type="primary"):
    st.session_state.schedule_generated = True

if st.session_state.schedule_generated:
    # Retrieve tasks through Scheduler -> Owner.get_all_tasks().
    all_tasks = scheduler.organize_tasks()

    if not all_tasks:
        st.info("No tasks scheduled yet. Add a task to get started.")

    else:
        # Sort tasks chronologically by scheduled time.
        sorted_tasks = sorted(
            all_tasks,
            key=lambda task: datetime.strptime(
                task.time,
                "%I:%M %p",
            ),
        )

        for index, task in enumerate(sorted_tasks):
            # Find which pet owns this task.
            task_pet = next(
                (
                    pet for pet in owner.pets
                    if task in pet.tasks
                ),
                None,
            )

            pet_label = task_pet.name if task_pet else "Unknown pet"

            st.markdown(f"### {task.time} — {task.description}")

            st.write(
                f"**Pet:** {pet_label}  \n"
                f"**Frequency:** {task.frequency}  \n"
                f"**Status:** "
                f"{'✅ Completed' if task.completed else '⏳ Pending'}"
            )

            # Update the actual Task object when clicked.
            if not task.completed:
                if st.button(
                    "Mark as complete",
                    key=f"complete_task_{index}",
                ):
                    scheduler.complete_task(task)
                    st.rerun()
            else:
                st.success("This task is completed.")

            st.divider()

        st.caption(
            f"Showing {len(all_tasks)} task(s) across "
            f"{len(owner.pets)} pet(s)."
        )
