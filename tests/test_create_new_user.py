import pytest
import uuid

@pytest.mark.parametrize("first_name, last_name", [("Test", "User")])
def test_create_user_valid(page, first_name, last_name):
    unique_email = f"{first_name.lower()}.{last_name.lower()}.{uuid.uuid4().hex[:6]}@example.com"

    # Click the "Add User" button
    # id="button-addNewUser"
    page.click("text='Add User'")

    # Fill out the Add User form
    page.fill("input[id='textfield-adduser-firstname']", first_name)
    page.fill("input[id='textfield-adduser-lastname']", last_name)
    page.fill("input[id='textfield-adduser-email']", unique_email)

    # Click the Save button
    # id="button-adduser-submit"
    page.click("button:has-text('Save')")

    # Confirm drawer closes and success message appears
    # Toastify toaster notfication
    # I think the id="top-center" ?
    page.wait_for_selector("text='User added successfully'", timeout=5000)

    # Optional: verify the new user appears at the top of the list
    page.wait_for_timeout(1000)
    row_selector = f"text='{first_name} {last_name}'"
    assert page.is_visible(row_selector), "New user row not found in list"
