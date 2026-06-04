## 2️⃣3️⃣ Day - 23

### Topics Covered:
Synchronization, Implicit Wait, Explicit Wait, Conditions to Learn, Import statements

### Problems:
- **Replace all time.sleep()**
In login and form automation, remove time.sleep() use WebDriverWait
- **Wait for Login Success Message**
Use https://the-internet.herokuapp.com/login?utm_source=chatgpt.com
After login, wait for: flash message using visibility_of_element_located
- **Wait for Clickable Button**
Use: element_to_be_clickable before clicking login button
- **Delayed Element Handling**
Use: https://the-internet.herokuapp.com/dynamic_loading/1?utm_source=chatgpt.com
Automate:
    1. click Start
    2. wait for Hello World text
    3. print text
- **Presence vs Visibility**
Use: presence_of_element_located & visibility_of_element_located
    
### Mini Project:

### Dynamic Login Automation Suite
#### Folder Structure:
selenium-python-automation/
│
├── day4_waits/
│   ├── implicit_wait.py
│   ├── explicit_wait.py
│   ├── dynamic_loading.py
│   ├── login_waits_project.py
│   │
│   └── utils/
│       └── waits.py

#### Features:
Program should:
- open login page
- wait for username field
- enter credentials
- wait for login button clickable
- click login
- wait for success message
- validate login
- logout
- validate logout

#### Requirements
MUST use:
- explicit waits
- reusable validation function
- reusable wait function

#### Reusable Wait Utility Task
- Create utils/waits.py.
Add reusable functions:
wait_for_visibility()
wait_for_clickable()

