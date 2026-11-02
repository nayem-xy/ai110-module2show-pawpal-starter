
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

    all_tasks = scheduler.sort_by_time()

    if not all_tasks:
        st.info("No tasks scheduled yet. Add a task to get started.")

    else:
        # Check the complete schedule for conflicts.
        conflicts = scheduler.detect_conflicts()

        if conflicts:
            st.warning(
                "Scheduling conflicts detected! Please review these tasks.")

            for conflict in conflicts:
                st.write(f"⚠️ {conflict}")
        else:
            st.success("No scheduling conflicts detected.")

        # Allow users to filter the schedule.
        st.markdown("### Filter Schedule")

        pet_options = ["All Pets"] + [
            pet.name for pet in owner.pets
        ]

        selected_filter_pet = st.selectbox(
            "Filter by pet",
            pet_options,
            key="schedule_pet_filter",
        )

        selected_status = st.selectbox(
            "Filter by status",
            ["All Tasks", "Pending", "Completed"],
            key="schedule_status_filter",
        )

        # Use Scheduler methods to retrieve filtered tasks.
        if selected_status == "Pending":
            filtered_tasks = scheduler.filter_by_status(
                completed=False
            )
        elif selected_status == "Completed":
            filtered_tasks = scheduler.filter_by_status(
                completed=True
            )
        else:
            filtered_tasks = scheduler.get_tasks()

        if selected_filter_pet != "All Pets":
            pet_tasks = scheduler.filter_by_pet(
                selected_filter_pet
            )
            filtered_tasks = [
                task for task in filtered_tasks
                if task in pet_tasks
            ]

        # Keep the filtered results in chronological order.
        sorted_tasks = [
            task for task in all_tasks
            if task in filtered_tasks
        ]

        st.markdown("### Scheduled Tasks")

        if not sorted_tasks:
            st.info("No tasks match your selected filters.")

        else:
            for index, task in enumerate(sorted_tasks):

                # Identify the pet assigned to this task.
                task_pet = next(
                    (
                        pet for pet in owner.pets
                        if task in pet.tasks
                    ),
                    None,
                )

                pet_label = (
                    task_pet.name if task_pet else "Unknown pet"
                )

                st.markdown(
                    f"### {task.due_date.strftime('%b %d, %Y')} "
                    f"— {task.time} — {task.description}"
                )

                st.write(
                    f"**Pet:** {pet_label}  \n"
                    f"**Frequency:** {task.frequency}  \n"
                    f"**Status:** "
                    f"{'✅ Completed' if task.completed else '⏳ Pending'}"
                )

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
            f"Showing {len(sorted_tasks)} of "
            f"{len(all_tasks)} task(s) across "
            f"{len(owner.pets)} pet(s)."
        )
