import pytest

# DELETE
@pytest.mark.order(5)
def test_delete_user(page, test_identity):
    email = test_identity["email"]

    # Locate the user row by email
    row = page.locator(f"table#virtualTable tbody tr:has-text('{email}')").first
    name_button = row.locator("[data-testid='user-name-in-list']")
    name_button.click()

    # Wait for drawer to load
    page.locator("input[id='textfield-modifyuser-firstname']").wait_for(timeout=10000)

    # Click the "Delete" button
    page.click("button:has-text('Delete')")

    # Wait for confirmation modal to appear
    modal = page.locator("div[role='dialog']:has-text('Are you sure')")
    modal.wait_for(timeout=5000)

    # Confirm modal text
    assert modal.locator("text=Please Confirm").is_visible()
    assert modal.locator("text=Are you sure you want to update status of this user?").is_visible()

    # Click "Confirm" in modal
    modal.locator("button:has-text('Confirm')").click()

    # Wait for success toast
    page.wait_for_selector("text=User status updated successfully", timeout=5000)

    # Validate the user is no longer in the table
    page.wait_for_timeout(1000)  # brief delay for UI update
    assert page.locator(f"table#virtualTable tbody tr:has-text('{email}')").count() == 0, "User still appears in list after deletion"