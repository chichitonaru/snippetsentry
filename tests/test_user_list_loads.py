import pytest

# READ
@pytest.mark.order(2)
def test_user_list_loads_successfully(page, test_identity):
    # Sanity check: confirm user list and Add User button is present
    assert page.locator("text='Add User'").is_visible()

    # Confirm expected columns exist
    expected_columns = ["Name", "STATUS", "Email", "Phone", "Android", "WhatsApp", "iMessage"]
    for col in expected_columns:
        assert page.locator(f"th:has-text('{col}')").is_visible()

    # Get the latest user (row 1 is the newest, 0 is usually spacer)
    row = page.locator("table#virtualTable tbody tr").nth(1)
    name_button = row.locator("[data-testid='user-name-in-list']")
    name = name_button.inner_text().strip()

    email_cell = row.locator("td").nth(4)
    email = email_cell.inner_text().strip()

    # Click the user's name to open the Modify User drawer
    name_button.click()

    # Wait for First Name input to appear in the drawer
    page.locator("input[id='textfield-modifyuser-firstname']").wait_for(timeout=10000)

    # Validate drawer contents match the table
    first_name_val = page.locator("input[id='textfield-modifyuser-firstname']").input_value()
    last_name_val = page.locator("input[id='textfield-modifyuser-lastname']").input_value()
    email_val = page.locator("input[id='textfield-modifyuser-email']").input_value()

    expected_first, expected_last = name.split(" ", 1)

    assert first_name_val == expected_first, "First name mismatch"
    assert last_name_val == expected_last, "Last name mismatch"
    assert email_val == email, "Email mismatch"
