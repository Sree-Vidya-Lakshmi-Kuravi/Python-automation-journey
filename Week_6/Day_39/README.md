# 🧪 Selenium Pytest POM (Page Object Model) Framework

An automated end-to-end testing framework built using **Python**, **Selenium WebDriver**, and **Pytest**. 

This framework tests the core e-commerce workflow of [SauceDemo](https://www.saucedemo.com) (login, inventory inspection, shopping cart actions, and checkout flow).

---

## 🎯 What Problem Does This Framework Solve?

When writing automated web tests, beginners often write single, messy scripts that hardcode URLs, usernames, and browser setups directly into the test code. 

**Why is that a problem?**
* If a web page changes a button's ID, you have to fix it in different places.
* If you want to run tests on **Edge** instead of **Chrome**, you have to edit every single test file.
* If credentials or URLs change, your code breaks.

### The Solution: 3 Core Design Patterns

This framework solves these issues using three industry-standard software design concepts:

1. **Page Object Model (POM):** We treat each web page (Login, Cart, Checkout) as a Python class. Tests don't interact with raw HTML directly—they call human-readable page methods like `login_page.login()`.
2. **Driver Factory Pattern:** A single "factory" module (`driver_factory.py`) creates and configures the browser. Tests simply ask for a browser without worrying about how it's created.
3. **Configuration Management (`config.ini`):** All URLs, credentials, timeouts, and browser choices are stored in a simple configuration file. Changing settings requires zero code edits!

---

## 📁 Project Architecture & Structure

selenium-pom-framework/
│
├── config/                  # ⚙️ Configuration Zone
│   ├── config.ini           # Key-value settings (URLs, browser selection, credentials)
│   └── config_reader.py     # Python reader that fetches config values safely
│
├── drivers/                 # 🌐 Browser Management
│   └── driver_factory.py    # Creates Chrome or Edge driver instances based on config.ini
│
├── pages/                   # 📄 Page Object Model (POM) Layer
│   ├── base_page.py         # Parent class with shared helper methods (click, type, wait)
│   ├── login_page.py        # Locators & actions for the Login Page
│   ├── inventory_page.py    # Locators & actions for the Product Catalog
│   ├── cart_page.py         # Locators & actions for the Shopping Cart
│   └── checkout_page.py     # Locators & actions for the E-Commerce Checkout Form
│
├── tests/                   # 🧪 Automated Test Suite
│   ├── test_login.py        # Validates login (successful & locked-out user scenarios)
│   ├── test_inventory.py    # Validates product listings and item counts
│   ├── test_cart.py         # Validates adding/removing items from the cart
│   └── test_checkout.py     # End-to-End test: Full purchase flow from start to finish
│
├── utils/                   # 🛠️ Framework Utilities
│   └── waits.py             # Explicit wait wrappers (WebDriverWait)
│
├── conftest.py              # Pytest fixture setup & teardown logic
├── pytest.ini               # Pytest configurations, flags, and custom test tags
└── README.md                # Project documentation