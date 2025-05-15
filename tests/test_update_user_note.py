import pytest
import uuid

# UPDATE
@pytest.mark.order(3)
def test_update_user_note(page, test_identity):
    email = test_identity["email"]
    test_note = f"Autotest Note {uuid.uuid4().hex[:4]}"

    # Locate the correct row by email
    row = page.locator(f"table#virtualTable tbody tr:has-text('{email}')").first
    name_button = row.locator("[data-testid='user-name-in-list']")
    name_button.click()

    # Wait for drawer to open by checking First Name input
    page.locator("input[id='textfield-modifyuser-firstname']").wait_for(timeout=10000)

    # Fill the notes field (it's an input)
    page.fill("input[id='textfield-modifyuser-notes']", test_note)

    # Save the changes
    page.click("button:has-text('Save')")

    # Wait for confirmation banner
    page.wait_for_selector("text='User Updated successfully'", timeout=5000)

    # Click the "Cancel" button to close the drawer
    page.click("button:has-text('Cancel')")

    # Reopen and confirm note persisted
    row = page.locator(f"table#virtualTable tbody tr:has-text('{email}')").first
    row.locator("[data-testid='user-name-in-list']").click()
    page.locator("input[id='textfield-modifyuser-notes']").wait_for(timeout=5000)

    current_note = page.locator("input[id='textfield-modifyuser-notes']").input_value()
    assert current_note == test_note, "Note did not persist after update"
