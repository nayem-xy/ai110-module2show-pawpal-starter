# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.

Our initial UML design consists of four classes: Owner, Pet, CareTask, and DailyPlanner. The Owner class stores the owner's available time and preferences, while Pet stores pet information and care requirements. CareTask represents individual activities such as feeding, walking, medication, and grooming, including their duration and priority. DailyPlanner coordinates these classes to create a daily care schedule, check time constraints, prioritize tasks, and explain its decisions. The design keeps each class focused on a specific responsibility, making the system easier to implement in Python and integrate with Streamlit.

- What classes did you include, and what responsibilities did you assign to each?

The initial design included Owner, Pet, CareTask, and DailyPlanner. Each class had a separate responsibility: Owner managed owner information, Pet stored pet details, CareTask represented individual care activities, and DailyPlanner handled scheduling and organization.



Sample Output
Today's Schedule
================
6:00 PM - Play with the cat (Daily) [Pending]
8:00 AM - Morning walk (Daily) [Pending]
8:30 AM - Breakfast (Daily) [Pending]
9:00 AM - Feed the cat (Daily) [Pending]



**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---Yes, our design changed during implementation. Instead of keeping the original CareTask and DailyPlanner classes, we implemented four classes named Task, Pet, Owner, and Scheduler. We also simplified the task attributes to focus on description, scheduled time, frequency, completion status, and due date. This made the design match the actual features we were able to implement. The Scheduler class became responsible for organizing tasks, filtering them, handling recurring tasks, and detecting conflicts. We updated the UML diagram to reflect the final Python implementation rather than keeping features that were only part of the original design.



## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

Our scheduler mainly considers the scheduled date, time, frequency, and completion status of each task. It sorts tasks chronologically so the owner can see what needs to be done and when. It also checks for conflicts between pending tasks that have the same date and time. I focused on these constraints because they were the most important for creating a simple and useful pet care schedule. Although the original design included task duration and priority, I decided to focus on the scheduling features that could be implemented and tested reliably within the project scope.



**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---One tradeoff I made in my scheduler was using exact-time matching for conflict detection instead of checking whether task durations overlap. This approach is easier to implement and understand, and it allows the scheduler to warn users when two tasks are scheduled for the same time. However, it cannot identify situations where one task starts before another task finishes. A more advanced version could include task durations and compare the time intervals. I decided to start with exact-time matching to keep the scheduling logic simple and manageable.

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI as a learning and development assistant throughout different stages of the project. It helped me understand how to organize the classes, work through Python logic, identify possible errors, and come up with test cases for important scheduling behaviors. I also used it to understand how the backend classes connect to the Streamlit interface. The most helpful prompts were specific questions about how a particular method worked, why an error was happening, or how I could test a certain feature. Breaking the work into smaller steps helped me understand the code instead of simply accepting a complete solution.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---One example was when AI suggested adding task durations and checking for overlapping time intervals to make conflict detection more advanced. I decided not to add that feature because it would expand the project beyond the scheduling behavior I had already implemented and tested. Instead, I kept conflict detection focused on tasks scheduled for the exact same date and time. I also verified the scheduling logic by running the test suite and checking whether the results matched the expected behavior. This helped me understand that AI suggestions can be useful, but I still need to make decisions based on the project requirements and verify the results myself.

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

Task completion: Verifies that tasks can be marked as completed.

Task sorting: Checks that tasks are arranged in chronological order.

Daily and weekly recurrence: Verifies that recurring tasks generate their next occurrence after completion.

Conflict detection: Checks whether pending tasks scheduled at the same date and time are flagged.

Date handling: Confirms that tasks scheduled at the same time on different dates are not treated as conflicts.

Task filtering: Tests filtering tasks by pet and completion status.

Empty schedules: Checks that the scheduler handles pets with no tasks.

These tests were important because they helped verify that the main scheduling features worked as expected and that the system could handle different situations, including empty schedules and tasks scheduled on different dates.

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with how the different classes work together to manage pet care tasks. I started with the system design and gradually connected the Python logic to the Streamlit interface. I especially liked implementing recurring tasks and conflict detection because they made the application more useful than simply storing a list of activities. I am also happy that I was able to write tests for the main features and get all 16 tests passing.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would improve the scheduling system by adding task duration and priority. This would allow the application to consider how long each activity takes and which tasks should be completed first. I would also like to add editing and deleting options for pets and tasks, along with a more advanced scheduling system that considers the owner's available time. These improvements would make PawPal+ more flexible and practical for everyday use.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One important thing I learned is that designing a system and actually implementing it are two different challenges. An initial design can include many ideas, but during implementation, I need to consider what is realistic, manageable, and testable. I also learned that AI can be a helpful tool for understanding concepts, debugging, and exploring possible solutions, but it should not make every decision for me. I still need to understand the code, evaluate suggestions, and verify that the final system works as expected.