import pytest
from playwright.sync_api import sync_playwright
import uuid

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

    # Login
    page.fill("#input-v-2", "george.mandella@gmail.com")
    page.fill("#input-v-4", "Snippler69!")

    login_button = page.locator("button[type='submit']")
    login_button.wait_for(state="attached")
    login_button.wait_for(state="visible")
    while login_button.is_disabled():
        page.wait_for_timeout(100)
    login_button.click()

    page.wait_for_url("**/dashboard", timeout=10000)
    page.goto("https://beta.snippetsentry.com/app/client/users")
    page.wait_for_selector("text='Add User'", timeout=10000)

    yield page
    page.close()

@pytest.fixture(scope="session")
def test_identity():
    uid = uuid.uuid4().hex[:6]
    first = f"Test{uid}"
    last = f"User{uid}"
    email = f"{first.lower()}.{last.lower()}@example.com"
    return {"first_name": first, "last_name": last, "email": email}
