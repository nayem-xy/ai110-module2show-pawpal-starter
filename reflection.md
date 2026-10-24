# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.

Our initial UML design consists of four classes: Owner, Pet, CareTask, and DailyPlanner. The Owner class stores the owner's available time and preferences, while Pet stores pet information and care requirements. CareTask represents individual activities such as feeding, walking, medication, and grooming, including their duration and priority. DailyPlanner coordinates these classes to create a daily care schedule, check time constraints, prioritize tasks, and explain its decisions. The design keeps each class focused on a specific responsibility, making the system easier to implement in Python and integrate with Streamlit.

- What classes did you include, and what responsibilities did you assign to each?


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

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
