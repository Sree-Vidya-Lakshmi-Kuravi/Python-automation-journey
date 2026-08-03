## Enterprise API Automation Framework
### Project Overview
This project is an automated testing framework built to test REST APIs. It automatically sends requests (GET, POST, PUT, PATCH, DELETE) to an API server, validates the responses, checks data schemas, and generates logs and visual test reports.

### Features
- No Code Duplication: Uses a single request function to handle all HTTP calls and logging automatically.
- Class-Free Structure: Built entirely using simple Python functions.
- Data-Driven Testing: Runs tests using data from JSON, CSV, or Excel files without changing test code.
- Automatic Logging: Saves every request, response, status code, and execution time into log files automatically.
- Schema Validation: Verifies API response structures against defined JSON schemas.
- Dual Reporting: Automatically generates standard HTML reports and Allure visual reports.

### Tech Stack
- Language: Python
- Test Runner: PyTest
- HTTP Client: Requests
- Schema Validation: JSONSchema
- Data Readers: Pandas, OpenPyXL
- Reporting: PyTest-HTML, Allure-PyTest

### Installation
- Clone or open the project folder:
    cd api-automation-framework-project
- Install required packages:
    pip install -r requirements.txt
- Execution
    Run all tests: pytest
- HTML Report: Generated automatically after each run inside:
    reports/report.html
- Allure Report: To view the Allure report dashboard in your browser, run:
    allure serve reports/allure-results

### Future Enhancements
- Integrate with CI/CD tools like GitHub Actions or Jenkins.
- Add database validation checks for backend verification.
- Add Slack or Email notifications upon test suite completion.