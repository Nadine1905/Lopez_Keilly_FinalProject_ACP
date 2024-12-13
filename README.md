I.	PROJECT OVERVIEW
TaskTok is a useful tool designed to make task management and account organization simpler and more efficient. As a user friendly platform, it helps users stay on top of their daily responsibilities. The system tackles common challenges like tracking task progress, managing accounts, and ensuring seamless updates. By automating essential features such as task creation, progress tracking, and account maintenance, TaskTok minimizes the effort needed to manage daily activities while ensuring accuracy and reliability. The platform enhances productivity and promotes accountability by giving users the ability to easily create, update, delete, and mark tasks as completed. It also provides a clear overview of progress, making it easier to stay organized. TaskTok uses a centralized database to securely store user information and task details, ensuring quick access and error free records. Security is a top priority, with built in features like password encryption and account validation. Its clean, intuitive design, built using CustomTkinter makes it accessible to users of all experience levels.

What's different about TaskTok apart its customizable dashboard options, which lets users filter tasks by status and update account information with ease. This design helps users track their tasks easily and make adjustments as needed, keeping them motivated and on track. The system’s focus on simplicity ensures that it remains easy to use, avoiding unnecessary complexity.TaskTok is built to improve efficiency by offering seamless registration, secure logins, and real-time task updates. By cutting down on repetitive processes and streamlining how tasks are managed, it enables users to focus on their goals. Its primary purpose is personal task management, TaskTok has the potential to advance, with future plans to introduce features like reminders, data analytics, and mobile integration. The platform is versatile enough to suit a wide range of users, from students and professionals to anyone aiming to stay organized. Its straightforward design ensures that even those with limited technical know-how can use it without difficulty. Whether you’re looking to boost productivity or bring order to your day, TaskTok is a reliable companion to help you achieve your goals.


II.	PYTHON CONCEPTS AND LIBRARIES

1.	Tkinter and CustomTkinter:
•	Tkinter is a standard Python library used to create graphical user interfaces (GUIs). It provides tools to create windows, buttons, text fields, and other GUI elements.
•	CustomTkinter (imported as ctk) is an enhanced version of Tkinter, which offers customizable widgets with a more modern and appealing design. This library helps make the GUI look better and offers additional features like improved fonts and colors for a more polished look.
2.	MySQL Connector:
•	MySQL Connector (imported as mysql.connector) is a Python library that allows for easy interaction with MySQL databases. In the code, it is used to establish a connection to a database (tasktok_db), execute SQL queries, and manage user authentication and task management.
•	Key functions like connect() establish the connection to the database, while cur.execute() runs SQL queries to retrieve, insert, update, or delete records from the database.
3.	bcrypt:
•	bcrypt is a password hashing library. It securely hashes passwords, making them unreadable if accessed. In this code, bcrypt.hashpw() is used to hash passwords during user registration, and bcrypt.checkpw() verifies that the entered password matches the stored hash during login. This ensures password security by protecting users' sensitive data.
4.	Regular Expressions (re module):
•	The re module provides a way to work with regular expressions in Python, which allows for pattern matching within strings. The is_valid_email() function uses a regular expression to validate email addresses, ensuring they follow the correct format (e.g., user@example.com).
5.	Error Handling with Try/Except:
•	The code uses the try and except blocks to handle potential errors during database interactions or user input. For example, in the connect() function, if a database connection fails, an error message is displayed using messagebox.showerror(). This prevents the application from crashing and provides helpful feedback to the user.
6.	User Interface Design:
•	The code uses both Tkinter and CustomTkinter to design user interfaces for login, registration, and managing tasks. The CTkFrame, CTkLabel, CTkEntry, and CTkButton widgets are used extensively to build the structure, input fields, and buttons in the GUI, enabling users to interact with the application smoothly.
7.	Classes:
•	The program is structured using classes, which helps in organizing and managing different parts of the application. Classes like LoginRegister, Login, Register, Dashboard, and others encapsulate the logic and layout for each screen. This approach enhances code reusability, readability, and maintainability.

III.	SUSTAINABLE DEVELOPMENT GOALS

1.	SDG 3: Good Health and Well-Being
•	The app helps users organize their tasks effectively. A well-organized schedule can reduce stress, promote mental health, and enhance overall well-being by enabling users to stay on top of their responsibilities.
•	By offering a structured way to track progress and complete tasks, the application can help users manage workloads and avoid burnout, which contributes to good mental health.

2.	SDG 4: Quality Education
•	The app's organization of tasks can also benefit students or learners who need to keep track of their study schedules, assignments, and deadlines, thereby supporting their educational goals.
•	By promoting productivity and time management skills, the app can indirectly encourage lifelong learning and improve learning outcomes for users, particularly in academic environments.

3.	SDG 8: Decent Work and Economic Growth
•	By allowing users to manage tasks effectively, the app aids in productivity. It can be used by professionals, students, or anyone managing multiple tasks, helping improve efficiency in work and study settings.
•	Good task management can support better career outcomes and professional growth, as users can meet deadlines, reduce procrastination, and improve job performance.

4.	SDG 9: Industry, Innovation, and Infrastructure
•	The app is an example of innovative use of technology to improve personal productivity. It integrates features like secure authentication (via password encryption), database interactions, and task management, which could be useful for both personal and professional settings.

5.	SDG 10: Reduced Inequality
•	The app is available to anyone with access to a computer, thus helping to bridge digital divides. By providing a tool that aids in personal productivity and organization, it can empower individuals from different backgrounds to improve their lives.

IV.	PROGRAM/SYSTEM INSTRUCTIONS

System Requirements:
1.	Software Prerequisites:
•	Python 3.8 or higher.
•	Required Python libraries:
•	tkinter
•	customtkinter
•	mysql-connector-python
•	bcrypt
2.	Database Configuration:
•	Install MySQL Server.
•	Create a database named tasktok_db.
•	Create the required tables to run the program:

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    status ENUM('pending', 'completed') DEFAULT 'pending',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

II. Application Workflow

1.	Login and Registration:
•	Launch the app to view options for Login or Register.
•	Login requires a valid email/username and password combination.
•	Register prompts the user to create a unique username, provide a valid email, and set a password.

2.	Menu Dashboard:
•	After login, the user is redirected to the Dashboard.
•	Available actions:
•	Add Tasks
•	View Tasks
•	Account Settings
•	Logout
•	Exit

3.	Task Management:
•	Add Task: Enter a task name and save it.
•	View Tasks: Displays all tasks with options to:
•	Mark as Completed
•	Redo (revert to pending)
•	Delete tasks.

4.	Account Settings:
•	View and update username and email.
•	Option to delete the account.

5.	Logout:
•	Securely log out and return to the main login/register screen.

III. Usage Instructions
1.	Installing Required Libraries: Use pip to install dependencies:
•	pip install mysql-connector-python bcrypt customtkinter

2.	Running the Application:
•	Save the script as tasktok.py.
•	Run the script:
python tasktok.py

3.	Database Connection: Ensure MySQL is running locally with a user root and no password. Modify the connect function to fit your database credentials if necessary.

4.	Error Handling:
•	Database errors are displayed as messages.
•	Invalid email or login attempts trigger pop-ups with error details.

IV. Core Functionalities
1.	Login Validation:
•	Supports email or username for authentication.
•	Uses bcrypt for secure password hashing and validation.

2.	Task Management:
•	Tasks are tied to user accounts and can be managed in a dedicated interface.
•	Task actions update statuses dynamically in the database.

3.	Account Management:
•	Users can update or delete their accounts. Deleting an account removes associated tasks.
