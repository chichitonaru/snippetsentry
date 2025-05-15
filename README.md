# SnippetSentry UI Automation

This project automates the UI testing of the "Manage Users" feature in SnippetSentry using Python, Playwright, and Pytest. It includes end-to-end tests covering the CRUD operations and critical user actions such as suspending and modifying users.

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/chichitonaru/snippetsentry.git
   cd snippetsentry
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

---

## Running the Tests

To execute the test suite:

```bash
pytest -v
```

The tests are ordered by execution sequence using `pytest-order`. Tests must run in sequence because a user is created at the beginning and then updated, suspended, and deleted across the suite.

---

## Tests Included

| Test File                  | Description                                      |
|---------------------------|--------------------------------------------------|
| `test_create_new_user.py` | Creates a new user                               |
| `test_user_list_loads.py` | Verifies that the user list is visible and accurate |
| `test_update_user_note.py`| Updates the note field for the created user      |
| `test_suspend_user.py`    | Suspends the user                                |
| `test_delete_user.py`     | Deletes the user                                 |

All tests include assertion steps and are intended to be run against the live beta site:  
`https://beta.snippetsentry.com/app/client/users`

---

## Notes

- All selectors were reverse-engineered from the production HTML via Playwright.
- The test plan follows the structure and expectations laid out in the SnippetSentry technical assessment.
- Test output and identity data can be inspected and debugged from the `test_identity` fixture shared in `conftest.py`.

---

## Requirements

- Python 3.9+
- `pytest`
- `playwright`
- `pytest-order`
