# Playwright Automation Framework (Python)

End-to-end UI automation framework built using Playwright, Pytest, and Page Object Model (POM) with CI/CD integration through GitHub Actions.

## Features

- Playwright with Python
- Pytest framework
- Page Object Model (POM)
- Cross-browser support
- Headless execution
- Screenshot capture on failure
- HTML reporting
- Parallel execution
- GitHub Actions CI/CD

## Project Structure

```bash
playwright_project/
│
├── pages/
├── tests/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .github/workflows/playwright.yml
```

## Setup

### Clone Repository

```bash
git clone https://github.com/pavan123chinta/playwright_automation.git
cd playwright_automation
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

## Run Tests

```bash
pytest
```

## Run Tests in Parallel

```bash
pytest -n 2
```

## Generate HTML Report

```bash
pytest --html=report.html
```

## CI/CD

GitHub Actions workflow runs automatically on push to the main branch.

## Test Application

https://opensource-demo.orangehrmlive.com

## Future Enhancements

- Allure Reports
- Retry failed tests
- Docker setup
- Environment-based configurations
- API + UI automation integration

## Author

Pavan Chinta  
QA Automation Engineer
