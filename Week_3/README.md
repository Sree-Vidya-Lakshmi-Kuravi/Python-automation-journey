## 1️⃣5️⃣ Day - 15

### Topics covered:
Modules, import keyword, custom modules, packages

### Problems:
- **Calculator Module**
    - Create calculator.py
    - Functions: add, subtract, multiply, divide
    - Create main.py and import calculator functions
- **String Utility Module**
    - Create string_utils.py
    - Functions: reverse string, palindrome check, vowel count
    - Use from another file
- **Math Utility Module**
    - Create math_utils.py
    - Functions: factorial, prime check, fibonacci
    - Import and test
- **Take the student management system project and convert it in project structure**
    
    student_management_system/
    │
    ├── main.py
    ├── student_manager.py
    ├── file_handler.py
    ├── utils.py
    └── data/
    └──── students.txt
    
    - **student_manager.py** contains class StudentManager
    - **file_handler.py** contains read data, save data
    - **utils.py** contains helper functions, validations
    - **main.py** contains menu, user interaction

### Challenges:
- Create **greetings.py.** Function: say_hello(). Import in **main.py**
- Create package **utils/** with __ **init __**.py, **math_utils.py, string_utils.py**. Import package modules.

## 1️⃣6️⃣ Day - 16

### Topics Covered:
Creating and activating virtual environments, pip commands, pip requests library
pip - Install package, View installed packages, Generate requirements.txt, Install from requirements.txt

### Problems:
- Simple GET Request
    Fetch: https://jsonplaceholder.typicode.com/users
- Print status code
    Use: response.status_code
- Convert response to JSON
    Use: response.json()
- Print User Names
    Loop through response data. Print: Name Email
- Fetch single user
    Try: /users/1

### Mini Project:

**User Data Fetcher**
Create user_fetcher.py

**Features:**
- Menu:
    1. Fetch all users
    2. Fetch single user
    3. Exit
- Use:
    - requests
    - functions
    - loops
    - exception handling


## 1️⃣7️⃣ Day - 17

### Topics Covered:
CSV Handling - import csv module, read csv file, write csv file, DictReader, DictWriter
JSON Handling - import json module, convert python to JSON, read JSON string, convert JSON string

### Problems:
**CSV Handling**
- Write student data to CSV. Create students.csv and store name, marks
- Read CSV data. Print Name: s_name Marks: s_marks
- Calculate Average Marks from CSV
- Search Student in CSV by name
- Add New Student into CSV

**JSON Handling**
- Store student data in JSON
- Read JSON Data and print all students
- Add new student to JSON
- Search student in JSON
- Convert Dictionary to JSON String

### Mini Project

**Employee Data Manager**
- Create employee_manager.py
- Features
    1. Add Employee
    2. View Employees
    3. Search Employee
    4. Save to JSON
    5. Export to CSV
    6. Exit
- Employee Structure
    {
    "name": "John",
    "department": "QA",
    "salary": 50000
    }
    
- Use: OOP, JSON, CSV, File handling, Exception Handling


## 1️⃣8️⃣ Day - 18 and 1️⃣9️⃣ Day - 19

### Task Manager Application
#### File Structure:
task_manager/
│
├── main.py
├── task_manager.py
├── file_handler.py
├── utils.py
├── data/
│   └── tasks.json
│
└── README.md

#### Features:
- **Add Task**
    - Enter task title, task description, choose priority - Low, High, Medium | Default status - Pending
- **View all Tasks**
    - Display all tasks clearly.
        
        ```xml
        ID: 1
        Title: Learn Selenium
        Priority: High
        Status: Pending
        ```
        
- **Search Task**
    - Search by title or task ID
    - If task exists: Task Found
    - Else: Task Not Found
- **Update Task Status**
    - User should be able to update: Pending → Completed or Pending → In Progress
- **Delete Task**
    - Delete task using Task ID
- **Filter Tasks**
    - Show completed tasks
    - Show pending tasks
    - Show high priority tasks
- **Save tasks to JSON File**
    - Store all tasks in tasks.json
- **Load Existing tasks automatically**
- **Menu based system**
- **Exception Handling**
    - Invalid menu choice, invalid task id, missing json file, empty inputs, invalid status, invalid priority
- **Validation Rules**
    - Task title cannot be empty.
    - Priority only high/medium/low
    - Status only pending/in progress/completed
    - Task id must be unique
- **OOP Requirements**
    - Use class TaskManager
    - Methods: add_task(), view_tasks(), search_tasks(), update_tasks(), delete_task(), filter_tasks(), save_tasks(), load_tasks()
- **File Separation requirements**
    - main.py - Contains menu, user interaction
    - task_manager.py - Contains TaskManager class
    - file_handler.py - Contains JSON read/write functions
    - utils.py - Contains validations, helper functions
- **Export tasks to csv**
- **Add due date**
- **Sort tasks -** Sort by priority, status
- **Task statistics -** Display:
    Completed Tasks: 5
    Pending Tasks: 2
- **Search by priority**

## 2️⃣0️⃣ Day - 20

### Topics Covered:
Selenium - Learn basic browser operations, maximize window, print current URL, open another website, learn browser DevTools

### Problems:
- Create browser_operations.py. Program should:
    - Open browser
    - Maximize window
    - Open google
    - Print title
    - Print current URL
    - Open github
    - Print title
    - Close browser

## 2️⃣1️⃣ Day - 21

### Topics Covered:
Locators - id, name, tag_name, xpath, css selector

### Problems:
- Open https://google.com. Locate search box. Search Selenium Python. Print title
- Login automation. Use: https://the-internet.herokuapp.com/login. Automate complete login
- Print page elements - page title, current URL, success message

## 2️⃣2️⃣ Day - 22

### Topics Covered:
Learn clear(), Learn .text, get_attribute(), Form Automation

### Problem:
- Fill:
    - Full Name
    - Email
    - Current Address
    - Permanent Address
- Click submit
- Capture output. After submit print element.text for all generated results
- Validation

### Mini Project
- Create:
    
    day3/
    │
    ├── textbox_form.py
    ├── login_validation.py
    └── user_registration.py
    
- **user_registration.py**
    Automate complete form:
    1. Open DemoQA textbox page.
    2. Fill all fields.
    3. Submit.
    4. Capture output.
    5. Validate entered data against displayed data.
    6. Print: TEST PASSED or TEST FAILED
- Create reusable validation function:
def validate(actual, expected):
