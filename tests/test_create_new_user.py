import pytest

# CREATE
@pytest.mark.order(1)
def test_create_user_valid(page, test_identity):
    """Creates a new user with valid information and verifies the list and banner confirmation."""
    first_name = test_identity["first_name"]
    last_name = test_identity["last_name"]
    unique_email = test_identity["email"]

    # Click "Add User"
    page.click("#button-addNewUser")

    # Fill out the user form
    page.fill("#textfield-adduser-firstname", first_name)
    page.fill("#textfield-adduser-lastname", last_name)
    page.fill("#textfield-adduser-email", unique_email)

    # Submit
    page.click("#button-adduser-submit")
    page.wait_for_selector("text='User added successfully'", timeout=5000)

    # Find correct row
    row = page.locator(f"table#virtualTable tbody tr:has-text('{unique_email}')").first

    # First, Last name check
    name_cell = row.locator("[data-testid='user-name-in-list']")
    assert name_cell.inner_text().strip() == f"{first_name} {last_name}", "Name does not match"

    # Status check
    assert row.locator("text='Pending'").is_visible(), "Status is not 'Pending'"

    # Email check
    assert row.locator(f"text='{unique_email}'").is_visible(), "Email not found in row"

    # Optional fields check
    empty_cells = row.locator("td.text-center, td.custom-width").all()
    empty_texts = [cell.inner_text().strip() for cell in empty_cells]
    assert any(e == "" for e in empty_texts), "Expected one or more blank optional fields"
