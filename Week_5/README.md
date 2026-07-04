## 3️⃣0️⃣ Day - 30 to 3️⃣2️⃣ Day - 32

### Project
### SauceDemo E-Commerce Automation

#### Folder Structure
e_commerce_automation/
│
├── day_30_login_tests.py
├── day_30_product_tests.py
├── day_31_cart_tests.py
├── day_32_checkout_tests.py
│
├── utils/
│   ├── waits.py
│   ├── validation_utils.py
│   ├── take_screenshot.py
│   ├── reusable_func.py
├── screenshots/
├── logs/

#### Tasks
- Positive Login
- Negative Login
- Product Inventory Validation
- Product Information Validation
- Add single product to cart
- Add multiple products to cart
- Cart Validation
- Remove Product from cart
- Screenshot Utility Usage
- Exception Handling
- Checkout Information
- Checkout overview validation
- Complete order
- Success validation
- Screenshot capture
- Logging
- End to end flow script




## 3️⃣3️⃣ Day - 33
## PyTest Fundamentals

### Topics Covered
Setup PyTest, PyTest Basics, Test Naming, Assertionns, Test Discovery, Running Tests

#### Folder Structure
Day_33/
├── test_google.py

#### Tasks
- Valid login
- Invalid login
- Product Count
- Product Exists
- Logout Test




# 3️⃣4️⃣ Day - 34
## Pytest Fixtures

### Topics Covered
Pytest Fixtures, Fixture Syntax, yield vs return, conftest.py

#### Folder Structure
Day_34/
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   └── test_cart.py
├── conftest.py

#### Tasks
- Create a login fixture
- Create a browser fixture
- Create multiple tests using the same fixture




# 3️⃣5️⃣ Day - 35
## Pytest Markers

### Topics Covered
Parameterization, Markers, Custom markers, pytest.ini file

#### Folder Structure
Day_35/
├── tests/
│   ├── test_login_creds.py
│   ├── test_product_cart.py
│   └── test_checkout_validation.py
├── marker_tests/
│   ├── test_smoke_login.py
│   ├── test_smoke_add_product.py
│   └── test_smoke_checkout.py
├── regression_tests/
│   ├── test_regression_login.py
│   ├── test_regression_add_product.py
│   └── test_regression_checkout.py
├── conftest.py
├── pytest.ini

#### Tasks
- Parameterize the valid login
- Parameterize the invalid login
- Parameterize the product validation
- Use smoke and regression