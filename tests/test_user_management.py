import pytest
import time
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

@pytest.fixture(scope="function")
def admin_dashboard(page):
    """Fixture to handle login and navigation to the Admin module once per test."""
    login = LoginPage(page)
    admin = AdminPage(page)

    login.navigate()
    login.login("Admin", "admin123")
    admin.navigate_to_admin()
    return admin

# TC-001: Add a Valid System User
def test_tc001_add_valid_user(admin_dashboard, page):
    admin = admin_dashboard
    unique_user = f"Tester_{int(time.time())}" # Ensures username is always unique

    admin.create_user("Admin", "a", "Enabled", unique_user, "Password@123")

    # Validation
    page.wait_for_selector("text=Success")
    admin.search_user(unique_user)
    assert page.locator(f"text={unique_user}").is_visible()

# TC-002: Add User with Existing Username (Negative)
def test_tc002_duplicate_username(admin_dashboard, page):
    admin = admin_dashboard
    admin.add_button.click()
    admin.username_input.fill("Admin")

    # Validation for "Already exists" error message
    error_msg = page.locator("xpath=//label[text()='Username']/parent::div/following-sibling::span")
    assert error_msg.text_content() == "Already exists"

# TC-003: Add User with Mismatched Passwords (Negative)
def test_tc003_mismatched_passwords(admin_dashboard, page):
    admin = admin_dashboard
    admin.add_button.click()
    admin.password_input.fill("Pass123")
    admin.confirm_password_input.fill("Wrong456")

    # Validation for "Passwords do not match"
    error_msg = page.locator("xpath=//label[text()='Confirm Password']/parent::div/following-sibling::span")
    assert error_msg.text_content() == "Passwords do not match"

# TC-004: Search for the newly created user
def test_tc004_search_user(admin_dashboard, page):
    admin = admin_dashboard
    # We search for the default 'Admin' user for verification
    admin.search_user("Admin")
    assert page.locator("text=Admin").first.is_visible()

# TC-005: Search using a Non-existent Username (Negative)
def test_tc005_search_non_existent(admin_dashboard, page):
    admin = admin_dashboard
    admin.search_user("NonExistentUserXYZ")
    
    # Validation
    assert page.locator("text=No Records Found").is_visible()

# TC-006: Edit User Details and Validate Update
def test_tc006_edit_user(admin_dashboard, page):
    admin = admin_dashboard
    # 1. First create a temporary user to edit
    temp_user = f"EditMe_{int(time.time())}"
    admin.create_user("Admin", "a", "Enabled", temp_user, "Password@123")
    
    # 2. Search and Edit
    admin.search_user(temp_user)
    page.locator(".bi-pencil-fill").click() # Click edit icon
    
    # Change status to Disabled
    admin.status_dropdown.click()
    page.get_by_role("option", name="Disabled").click()
    admin.save_button.click()
    
    # 3. Verify
    page.wait_for_selector("text=Success")
    admin.search_user(temp_user)
    assert page.locator("text=Disabled").is_visible()

# TC-007: Delete the User
def test_tc007_delete_user(admin_dashboard, page):
    admin = admin_dashboard
    # 1. Create a user to delete
    del_user = f"DeleteMe_{int(time.time())}"
    admin.create_user("Admin", "a", "Enabled", del_user, "Password@123")
    
    # 2. Search and Delete
    admin.search_user(del_user)
    page.locator(".bi-trash").click()
    page.get_by_role("button", name="Yes, Delete").click()
    
    # 3. Verify
    page.wait_for_selector("text=Success")
    admin.search_user(del_user)
    assert page.locator("text=No Records Found").is_visible()