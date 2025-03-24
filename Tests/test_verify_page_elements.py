import re
from playwright.sync_api import Page, expect

# Variables
URL = "https://playwright.dev/"
PAGE_TITLE = "Playwright"
LINK_NAME = "Get started"
HEADING_NAME = "Installation"

def test_has_title(page: Page):
    page.goto(URL)
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile(PAGE_TITLE))

def test_verify_get_started_link(page: Page):
    page.goto(URL)
    # Click the get started link.
    page.get_by_role("link", name=LINK_NAME).click()
    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name=HEADING_NAME)).to_be_visible()