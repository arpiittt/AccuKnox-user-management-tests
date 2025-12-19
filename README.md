AccuKnox User Management & System Monitoring Suite
==================================================

📌 Project Overview
-------------------

This repository contains a dual-purpose solution developed for the AccuKnox technical assessment:

1.  **Automated E2E Testing**: A robust Playwright-based test suite for the OrangeHRM User Management module.

2.  **System Monitoring Tools**: Python scripts for log analysis and website health monitoring.

* * * * *

🏗️ Architecture: Page Object Model (POM)
-----------------------------------------

The automation project is structured using the **Page Object Model** to ensure maintainability and scalability:

-   **`pages/`**: Encapsulates page-specific locators and actions. Uses advanced locator strategies like **Relational XPath** and **Aria Roles** to ensure test stability.

-   **`tests/`**: Contains the test logic. Leveraging `pytest` fixtures, the suite maintains test isolation by handling authentication independently for each case.

* * * * *

🧪 Automated Test Cases
-----------------------

The suite covers 7 critical scenarios:

-   **TC-001**: Successful creation of a new system user.

-   **TC-002**: Validation for duplicate usernames (Negative).

-   **TC-003**: Password mismatch validation during user creation (Negative).

-   **TC-004**: Verification of search functionality for existing users.

-   **TC-005**: Handling of "No Records Found" for non-existent users (Negative).

-   **TC-006**: End-to-end update flow (Editing user status).

-   **TC-007**: Full deletion cycle and confirmation.

* * * * *

🚀 Getting Started
------------------

### 1\. Prerequisites

Ensure you have Python 3.x installed. It is recommended to use a virtual environment.

### 2\. Installation

Bash

```
# Install required dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

```

### 3\. Running the Automation

To run the full test suite with a visible browser:

Bash

```
pytest -v --headed tests/test_user_management.py

```

### 4\. Running Monitoring Scripts

Bash

```
# Analyze access logs
python log_analyzer.py

# Check website health
python health_checker.py

```

* * * * *

⚠️ Important Note on Environment
--------------------------------

During development/execution, the public **OrangeHRM Demo** environment occasionally experiences **HTTP 500 Internal Server Errors** or **ERR_HTTP_RESPONSE_CODE_FAILURE**.

-   If the tests fail at the `login.navigate()` stage, please verify the site's status manually in a browser.

-   The script logic is verified and ready for execution once the environment is stable.

🛠️ Tech Stack
--------------

-   **Language**: Python 3.x

-   **Automation Library**: Playwright

-   **Test Runner**: Pytest

-   **Pattern**: Page Object Model (POM)

-   **Reporting**: Pytest Built-in Terminal Reporting

* * * * *

📂 Project Structure
--------------------

Plaintext

```
AccuKnox-user-management-tests/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   └── admin_page.py
├── tests/
│   ├── __init__.py
│   └── test_user_management.py
├── .gitignore            # Excludes venv and cache
├── log_analyzer.py       # System utility
├── health_checker.py     # System utility
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

```

* * * * *

### **Submission Checklist**

-   [x] All 7 Test Cases implemented.

-   [x] Page Object Model applied.

-   [x] Clean `.gitignore` included.

-   [x] All dependencies listed in `requirements.txt`.