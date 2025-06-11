# Experiences
---

## Full Stack Developer Intern
* **Organization:** Digio co,Ltd (Cooperative Program)
* **Duration:** June 2023 - September 2023
* **Institution:** Thai-Nichi Institute of Technology (TNI)
* **Setting:** My role centered on identifying and implementing improved solutions for challenges encountered within the team's projects. Due to the sensitivity of client data, my development and problem-solving tasks were conducted in a parallel environment, distinct from live systems, to ensure data confidentiality while directly supporting the team's objectives.

**General Responsibilities during Internship:**
* developed and implemented assigned projects/modules from senior engineer.
* dicussed on projects problems/solutions with senior engineer every morning.
* report what I had done at the end of the day.

**Key Projects & Contributions:**

**1. Ticket Support System**
* **Context & Purpose:** This system was designed to allow users to report issues and for administrators to manage and resolve these support requests efficiently.
* **My Role & Actions:**
    * Developed features for users to create new support tickets, including fields for title and description.
    * Implemented functionality for users to view their submitted tickets and their statuses.
    * Built the admin panel interface for managing all tickets, allowing administrators to view, assign, and provide solutions.
    * Integrated an email notification system to inform users when their tickets were resolved and closed. This included taking on board senior feedback, such as ensuring notifications were clear and considering that users should ideally be the ones to close their tickets.
    * Created a feature to export ticket data into an Excel report, which could be downloaded directly.
    * Developed a scheduled task to automatically generate and email a zipped Excel report of all tickets.
* **Technologies Used:** React (for UI components like forms and tables), Spring Boot (for backend logic, managing ticket data, and email services), MySQL (for storing ticket information).

**2. Data Reconciliation System**
* **Context & Purpose:** This system was developed to compare two datasets (e.g., "Data A" and "Data B," or "Existed Data" and "New Data") and identify discrepancies, reporting them as updated, new, or deleted entries.
* **My Role & Actions:**
    * Designed and implemented the core logic to compare records between two datasets and categorize the differences.
    * Developed the functionality to output the reconciliation results into an Excel file.
    * Created an admin interface allowing administrators to view reconciled data and potentially choose which version of the data should persist.
    * Researched and implemented different data processing methods, comparing sequential processing with parallel processing (multi-threading) for large datasets.
* **Key Achievement/Learning:** My approach to data processing in this system was recognized as an improvement by my seniors.This project provided significant insights into data comparison techniques and the practical considerations of choosing between sequential and parallel processing methodologies based on data volume and expected performance outcomes.

**Other Systems Contributed To:**

* **Registration & Login System:**
    * Implemented user registration forms and login functionality.
    * Integrated JSON Web Tokens (JWT) for secure authentication, including understanding its structure (header, payload, signature) and storage (e.g., in local storage).
    * Developed features for first-time password changes, one-time passwords (OTP), and a "forgot password" flow involving email verification.
    * Ensured all user passwords were encrypted before being stored in the database.
* **Manage User System:**
    * Created an admin panel for managing user information.
    * Implemented functionalities for admins to edit user details, delete users, and reset user passwords.
    * Integrated pagination to efficiently display and navigate through lists of users.
    * Developed a criteria-based query system to filter and search for specific users.

**Technical Stack & Concepts Applied:**

* **Frontend:** React (including React Router, Components, Services, Axios HTTP Library for API calls), understanding of React's Virtual DOM for efficient UI updates.
* **Backend:** Spring Boot (Spring REST Controller, Services, Repository, Model architecture).
* **Database:** MySQL.
* **Security & Authentication:** JWT implementation, password encryption.
* **Data Handling:** Data reconciliation, pagination, data filtering, file export (Excel), parallel vs. sequential processing. 

* **Key Learning from this Project:** This internship provided extensive hands-on experience in full-stack development within a professional environment. I deepened my understanding of building secure authentication systems, managing user data, developing practical support tools, and tackling complex data reconciliation tasks. A highlight was receiving positive feedback on my coding methods for the reconciliation system, and the practical experience gained in performance considerations for data processing.

---

## Teacher Assistance (TA)
* **Course & Institution:** "CPE-312 Microcontroller and Embedding System" - Thai-Nichi Institute of Technology (TNI)
* **Term:** November 2023 - Febuary 2024
* **Student Cohort:** Approximately 50 third-year undergraduate students with various skill levels and interest.

**Overall Role & Purpose:**
As a TA for CPE-312, my primary role was to support lecturer in delivering a positive and effective learning experience. This involved reinforcing core concepts in C programming for Microcontroller and Embedding System, facilitating practical application during lab sessions, and providing constructive guidance.

**Key Responsibilities & Activities:**

* **Leading Lab Sessions:**
    * I independently led two weekly lab sections of approximately 20 students each. My focus was on creating an interactive and supportive environment where students felt comfortable asking questions.
    * A significant part of my lab sessions involved actively answering student inquiries, assisting them with debugging their programming code in C language, and helping them troubleshoot issues with their electronic circuits.
* **Grading and Feedback:**
    * I was responsible for giving actionable feedback to weekly programming assignments and quizzes for roughly half the student cohort. And I was grading their final projects.
    * My approach to giving feedback was not just about right or wrong, but providing specific, actionable feedback to help students identify areas for improvement. For instance, instead of just saying "incorrect logic," I would often point to the specific lines of code and suggest how they might rethink their approach or refer them to relevant lecture material or datasheet. This often involved detailed comments in their code submissions.
* **Delivering Specialized Instruction:**
    * At the request of the lecturer, I prepared and delivered a dedicated lesson on Git version control. This initiative aimed to equip students with essential skills for managing their coding projects more effectively and fostering collaborative work.

**Challenges & How I Addressed Them:**

* **Varying Skill Levels:** A significant challenge in CPE-312 was addressing the diverse range of student abilities and engagement. Some students quickly grasped core concepts and were keen to explore more advanced questions, requiring me to do more research, provide supplementary materials or direct them to further resources to keep them stimulated. Another group needed more foundational support to build their understanding; for these students, I offered more targeted explanations and simplified examples during lab sessions and office hours, which typically enabled them to then proceed independently.
* **Maintaining Engagement in Labs:** Keeping all students engaged during a 3-hour lab session required active facilitation. I incorporated short, collaborative problem-solving activities and walked around constantly to check in with students individually, rather than just lecturing from the front.

**Skills Developed/Strengthened:**

* **Technical Communication:** Became adept at explaining complex programming concepts in simple, clear, and relatable terms to beginners.
* **Problem-Solving & Debugging:** Efficiently identifying and guiding students to resolve errors in code and circuit designs.
* **Instruction & Presentation:** Developing and delivering targeted lessons, such as the Git workshop.
* **Empathy & Patience:** Developed a greater understanding of the learning process and the importance of patience when students were struggling.
* **Mentorship & Guidance:** Honed my ability to guide students towards solutions rather than giving them direct answers, fostering their problem-solving skills.
* **Deeper Subject Matter Understanding:** Teaching Python fundamentals significantly solidified my own grasp of the language and core computer engineer principles.

---

## Machine Learning Teacher/Tutor
* **Context:** Volunteer Tutor
* **Audience:** An undergraduate student who can not understand college's Machine Learning lessons and Two graduated students who have no Machine Learning background but need to do research in Machine Learning and Deep Learning topic.
* **Period:** March 2025 - Present

**Key Activities & Teaching Approach:**

* **Curriculum & Material Development:**
    * For my workshops, I developed a 6-part introductory series covering:
        1.  Essential Python for ML
        2.  Numpy Stack (Numpy, Pandas, Matplotlib)
        3.  ML Core Concepts (Features, labels, ML Workflow, overfitting/underfitting)
        4.  Classical ML Algorithms (e.g., Linear Regression, K-Nearest Neighbors, Decision Trees – explained intuitively)
        5.  Hands-on Project (using Python and Scikit-learn).
        6.  Deep Learning Algorithms (Pytorch, Neural Network, Computer Vision, NLP)
    * I created presentations, Jupyter Notebooks with code examples, and curated small datasets for practical exercises.
* **One-on-One Tutoring:**
    * Sessions were highly personalized. Students would come with specific questions from their courses, personal projects, or general curiosity about ML.
    * My approach involved first understanding their current level of knowledge and then breaking down complex topics like gradient descent or backpropagation using analogies, visualizations, and step-by-step explanations. I often related concepts back to basic statistics or programming principles they already knew.
* **Interactive Workshops:**
    * In workshops, I focused on interactive learning. I'd pose questions, encourage group discussions, and include live coding sessions where participants could follow along and experiment.
    * For example, when explaining decision trees, I'd use a relatable, non-technical example first (like a flowchart for deciding what to wear based on weather) before introducing the technicalities.
* **Project Guidance:**
    * I helped several students conceptualize and troubleshoot their first ML projects, guiding them on data preprocessing, model selection, and interpretation of results.

**Challenges & How I Addressed Them:**

* **Abstract Nature of ML Concepts:** Many ML algorithms are mathematically intensive and abstract. The key challenge was making them intuitive without oversimplifying. I used a lot of visual aids, real-world examples (e.g., how spam filters work, how recommendation systems suggest movies), and focused on the 'why' behind an algorithm's design.
* **Varying Math/Programming Backgrounds:** Students came with different levels of preparedness in math and coding. For tutoring, I'd tailor the depth. In workshops, I'd provide optional "deeper dive" resources for those interested, while keeping the core content accessible. I also emphasized Python libraries like Scikit-learn that abstract away some of the more complex math for beginners.

**Skills Developed/Strengthened:**

* **Advanced Technical Explanation:** Mastered the ability to articulate highly complex topics like neural network architectures or ensemble methods in an understandable way for non-experts.
* **Curriculum Design:** Gained experience in structuring learning material logically and creating engaging educational content.
* **Adaptability in Teaching:** Learned to quickly assess a student's understanding and adjust my teaching style and depth of explanation accordingly.
* **Problem-Solving (for others):** Became proficient at diagnosing issues in students' ML code and conceptual misunderstandings.
* **Deepened ML Expertise:** The process of preparing to teach various ML topics significantly enhanced my own comprehensive understanding of the field.

---