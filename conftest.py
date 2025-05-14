import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    page.goto("https://beta.snippetsentry.com/login")

    # Fill in credentials
    page.fill("#input-v-2", "george.mandella@gmail.com")
    page.fill("#input-v-4", "Snippler69!")

    # Wait until login button is attached and visible
    login_button = page.locator("button[type='submit']")
    login_button.wait_for(state="attached")
    login_button.wait_for(state="visible")

    # Wait manually until it's enabled (Playwright doesn't support 'enabled' state directly)
    while login_button.is_disabled():
        page.wait_for_timeout(100)

    # Now click
    login_button.click()

    # Wait for successful login and redirect (initially to /dashboard)
    page.wait_for_url("**/dashboard", timeout=10000)

    # Navigate directly to the Manage Users page
    page.goto("https://beta.snippetsentry.com/app/client/users")

    # Confirm page is fully loaded by checking for the Add User button
    page.wait_for_selector("text='Add User'", timeout=10000)

    yield page
    page.close()
