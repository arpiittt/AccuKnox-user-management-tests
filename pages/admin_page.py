class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_menu = page.get_by_role("link", name="Admin")
        self.add_button = page.get_by_role("button", name="Add")

        # Form Locators (Using robust XPath for custom OrangeHRM elements)
        self.user_role_dropdown = page.locator("xpath=//label[text()='User Role']/parent::div/following-sibling::div")
        self.employee_name_input = page.get_by_placeholder("Type for hints...")
        self.status_dropdown = page.locator("xpath=//label[text()='Status']/parent::div/following-sibling::div")
        self.username_input = page.locator("xpath=//label[text()='Username']/parent::div/following-sibling::div//input")
        self.password_input = page.locator("xpath=//label[text()='Password']/parent::div/following-sibling::div//input")
        self.confirm_password_input = page.locator("xpath=//label[text()='Confirm Password']/parent::div/following-sibling::div//input")
        self.save_button = page.get_by_role("button", name="Save")

    def navigate_to_admin(self):
        self.admin_menu.click()

    def create_user(self, role, emp_name_hint, status, username, password):
        self.add_button.click()

        # Select Role
        self.user_role_dropdown.click()
        self.page.get_by_role("option", name=role).click()

        # Handle Employee Name Autocomplete
        self.employee_name_input.fill(emp_name_hint)
        self.page.locator(".oxd-autocomplete-option").first.click()

        # Select Status
        self.status_dropdown.click()
        self.page.get_by_role("option", name=status).click()

        self.username_input.fill(username)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)
        self.save_button.click()