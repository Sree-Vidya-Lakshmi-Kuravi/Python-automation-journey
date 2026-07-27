### 1. Why Page Object Model (POM)?
The Page Object Model (POM) is a structural design pattern that treats every web page of the application as an independent class object.
#### Key Benefits:
- Code Reusability: Page elements and common actions (e.g., login, button clicks) are written once in page classes and reused across multiple test cases.
- Maintainability: If an element's locator changes on the web page, you only update it in the corresponding page object file without altering any test scripts.
- Separation of Concerns: Test files focus purely on assertions and business workflow logic, while Page classes handle UI interactions and locators.


### 2. Why Driver Factory?
The Driver Factory pattern centralizes the instantiation, configuration, and teardown of the Selenium WebDriver instance.
#### Key Benefits:
- Cross-Browser Support: Easily switch between browsers (Chrome, Firefox, Edge) via configuration files or CLI options without altering test logic.
- Decoupled Setup: Isolates driver creation options (e.g., headless execution, window sizing, argument options) from individual test scripts.
- Clean Lifecycle Management: Pairs cleanly with Pytest fixtures (conftest.py) to handle session management, driver initialization, and teardown (driver.quit()) reliably.


### 3. Why Config Reader?
Hardcoding credentials, application URLs, or execution settings inside test code creates security risks and maintenance overhead. The Config Reader utility reads settings directly from a central config.ini configuration file.
#### Key Benefits:
- Environment Agility: Switch environments (e.g., Dev, QA, Staging) or browsers by changing a single key-value pair in config.ini.
- Security & Flexibility: Prevents sensitive data (like credentials) from being hardcoded inside test scripts.
- Centralized Control: Modifying global parameters (e.g., implicit wait timeouts, base URLs) takes effect across the entire framework instantly.


### 4. Logging Flow
The framework implements a Singleton Custom Logger utility to record granular runtime context during test execution.
#### Flow Architecture:
- Initialization: The CustomLogger utility creates a shared logger instance configuring both console output (CLI) and file output (logs/automation.log).
- Execution Tracking: Test actions, page interactions, and fixture events trigger log calls (logger.info(), logger.error()).
- Report Attachment: During test failures, the pytest_runtest_makereport hook in conftest.py automatically reads automation.log and attaches the log content directly to the corresponding Allure failure report.


### 5. Screenshot Flow
Capturing evidence upon test failure is crucial for rapid bug investigation and debugging.
#### Flow Architecture:
- Test Failure Event: When Pytest executes a test, the custom pytest_runtest_makereport hook monitors the execution phase outcome (call.when == "call").
- Detection & Capture: If a test fails (rep.failed), the hook extracts the active WebDriver instance attached to the Pytest node.


### 6. Storage & Allure Attachment
- A timestamped .png image file is captured and stored locally in the screenshots/ directory.
- The binary image payload is attached directly to the Allure Report under the failed test case (allure.attach).