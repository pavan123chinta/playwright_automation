import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("username,password,expected", [
    ("Admin", "admin123", "success"),
    ("Admin", "wrongpassword", "error"),
])
def test_login(page, base_url, username, password, expected):
    login_page = LoginPage(page)

    login_page.open(base_url)
    login_page.login(username, password)

    if expected == "success":
        assert login_page.is_login_successful()
    else:
        assert login_page.is_error_displayed()