import pytest

@pytest.mark.order(4)
def test_suspend_user(page, test_identity):
    email = test_identity["email"]

    # Locate the user row by email
    row = page.locator(f"table#virtualTable tbody tr:has-text('{email}')").first
    name_button = row.locator("[data-testid='user-name-in-list']")
    name_button.click()

    # Wait for drawer to open
    page.locator("input[id='textfield-modifyuser-firstname']").wait_for(timeout=10000)

    # Click the "Suspend" button
    page.click("button:has-text('Suspend')")

    # Wait for confirmation modal
    modal = page.locator("div[role='dialog']:has-text('Are you sure')")
    modal.wait_for(timeout=5000)

    # Confirm modal text is correct
    assert modal.locator("text=Please Confirm").is_visible()
    assert modal.locator("text=Are you sure you want to update status of this user?").is_visible()

    # Click Confirm
    modal.locator("button:has-text('Confirm')").click()

    # Wait for success banner
    page.wait_for_selector("text=User status updated successfully", timeout=5000)

    # Verify status has changed to "Suspended", retry for a few seconds to allow UI update
    page.wait_for_selector(f"table#virtualTable tbody tr:has-text('{email}') td:has-text('Suspended')", timeout=5000)

