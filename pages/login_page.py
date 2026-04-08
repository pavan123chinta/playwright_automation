class LoginPage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"
        self.dashboard_heading = "h6"
        self.error_message = ".oxd-alert-content-text"

    def open(self, base_url):
        self.page.goto(
            f"{base_url}/web/index.php/auth/login",
            wait_until="domcontentloaded"
        )
        self.page.wait_for_selector(self.username_input)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def is_login_successful(self):
        self.page.wait_for_selector(self.dashboard_heading)
        return "Dashboard" in self.page.text_content(self.dashboard_heading)

    def is_error_displayed(self):
        self.page.wait_for_selector(self.error_message)
        return "Invalid credentials" in self.page.text_content(self.error_message)