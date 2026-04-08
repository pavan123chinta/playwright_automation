import pytest
import os
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # ✅ FIX: Headless for CI/CD (GitHub Actions)
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def base_url():
    return "https://opensource-demo.orangehrmlive.com"


# 🔥 Screenshot on failure (FIXED + SAFE)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)  # ✅ ensure folder exists
            page.screenshot(path=f"screenshots/{item.name}.png")