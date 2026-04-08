Playwright Automation Framework (Python)

A robust end-to-end UI automation framework built using Playwright, Pytest, and Page Object Model (POM) with CI/CD integration using GitHub Actions.

Features

Playwright with Python
Pytest framework
Page Object Model (POM)
Cross-browser support (Chromium, Firefox, WebKit)
Headless execution (CI compatible)
Screenshot capture on failure
HTML reports
Parallel execution
GitHub Actions CI/CD

Project Structure

playwright_project/

pages/
init.py
login_page.py
google_page.py

tests/
init.py
test_login.py
test_google_test.py

screenshots/
conftest.py
requirements.txt
pytest.ini

.github/workflows/playwright.yml

Setup

Clone repository

git clone https://github.com/pavan123chinta/playwright_automation.git

cd playwright_automation

Create virtual environment

python -m venv venv
source venv/Scripts/activate

Install dependencies

pip install -r requirements.txt

Install Playwright browsers

playwright install

Run Tests

pytest

Run Parallel

pytest -n 2

Generate Report

pytest --html=report.html

Screenshots

Screenshots are automatically captured on failure and stored in the screenshots folder.

CI/CD (GitHub Actions)

Runs on every push to main branch
Installs dependencies
Runs tests in headless mode
Uploads report

Workflow file location:
.github/workflows/playwright.yml

Concepts Used

Page Object Model
Separates locators and actions from test logic

Pytest Fixtures
Reusable setup for browser, page, and base_url

Headless Execution
Required for CI/CD since no UI is available

Test Application

https://opensource-demo.orangehrmlive.com

Future Enhancements

Allure Reports
Retry failed tests
Docker setup
Environment-based configs
API + UI automation

Author

Pavan Chinta
QA Engineer
Skills: Playwright, Selenium, Python, UiPath
