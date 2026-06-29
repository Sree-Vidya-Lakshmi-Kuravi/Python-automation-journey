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
#### Folder Structure
Python-automation-journey/
│
├── day_23_waits/
│   ├── dynamic_loading.py
│   ├── explicit_wait.py
│   ├── implicit_wait.py
│   ├── logins_waits_project.py
│   ├── utils/

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



## 2️⃣4️⃣ Day - 24

### Topics Covered:
Waits, Implicit wait, Explicit waits



## 2️⃣5️⃣ Day - 25

### Topics Covered:
Dropdown Handling, Handle alerts, Switch windows/tabs, Switch frames/iFrames, Validate advanced interactions, ActionChains, Mouse Hover, Right Click, Double Click, Drag and Drop, Keyboard Actions

### Problems:
- Dropdown Automation
    Create: dropdown_handling.py
- Alert Automation
    Create: alerts_handling.py
- Window Handling
    Create: window_handling.py
- iFrame Handling
    Create: iframe_handling.py

### Mini Project

#### Advanced Interaction Automation Suite
#### Folder Structure
Python-automation-journey/
│
├── day25_adv_ops/
│   ├── dropdown_handling.py
│   ├── alerts_handling.py
│   ├── window_handling.py
│   ├── iframe_handling.py
│   ├── advanced_interactions_project.py
│   ├── screenshots/
├── day25_actionchains/
│   ├── actions.py
│   ├── drag_drop.py
│   ├── keyboard_actions.py
│   ├── mouse_hover.py
│   ├── screenshots/

Program should:
1. handle dropdown
2. handle alert
3. switch window
4. switch iframe
5. validate outputs
6. capture screenshots after each task
7. Action Chains
8. Mouse hover
9. Right Click
10. Double Click
11. Drag and Drop
12. Keyboard Actions



## 2️⃣6️⃣ Day - 26

### Topics Covered
JavaScript Executor, Scrolling, Hidden elements, Dynamic Elements, Advanced XPath

### Folder Structure
day26_javascript_dynamic/
│
├── dynamic_controls.py
├── scrolling.py
├── screenshots/

### Tasks:
- Print page title using JavaScript.
- Click a button using JavaScript.
- Highlight an element using JavaScript.
    Example:
    - change border color
    - change background color
- Scroll to bottom.
- Scroll to Submit button.
- Capture screenshot after scrolling.
- Add and remove checkboxes.
- Enable input field.



## 2️⃣7️⃣ Day - 27 and 2️⃣8️⃣ Day - 28

### Topics Covered
Web tables, Dynamic tables, Checkboxes, Radio buttons, Date Pickers

#### Folder Structure

day27_table_forms/
│
├── web_tables.py
├── dynamic_tables.py
├── checkboxes.py
├── radio_btn.py
├── date_picker.py
├── screenshots/

### Mini Project

#### Employee Management Validation Suite
#### Folder Structure
day27_emp_mgmt_validation/
│
├── employee.py
├── screenshots/

#### Features
- Add employee
- Search employee
- Validate employee exists
- Edit employee
- Use explicit waits
- Delete employee
- Validate deletion
- Capture screenshots
- Use reusable functions




## 2️⃣9️⃣ Day - 29

### Topics Covered
Logging, Screenshots, Assertions

### Mini Project

#### Login Validation Suite
#### Folder Structure
day27_report_validation/
│
├── logging_demo.py
├── logging_p.py
├── selenium_log.log
├── screenshots/

#### Features
- Positive Login: Validate URL, success msg
- Logging: Log every action
- Negative Login: Validate error msg
- Assertions: Use URL validation, text validation
- Screenshots: Capture success, failure
- Use exception handling
