import re
from playwright.sync_api import Page, expect
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
)

# Variables
URL = "https://playwright.dev/"
PAGE_TITLE = "Playwright"
LINK_NAME = "Get started"
HEADING_NAME = "Installation"
LINK_COMMUNITY = "Community"
HEADING_WELCOME = "Welcome"
LINK_AMBASSADOR = "Ambassador"
AMBASSADOR_IMAGE_TEXT = "Are you the next Ambassador?'"
LINK_DOCS = "Docs"
DOC_MENU_NAME = "Node.js"
DOC_PYTHON_NAME = "Playwright logo Playwright"
DOC_PYTHON_OPTION = "Python"

def test_has_title(page: Page):
    logging.info('Navigate to a page')
    page.goto(URL)
    logging.info('Verify the page title')
    expect(page).to_have_title(re.compile(PAGE_TITLE))

def test_verify_link_is_displayed(page: Page):
    logging.info('Navigate to a page')
    page.goto(URL)
    logging.info('Click on Get Started')
    page.get_by_role("link", name=LINK_NAME).click()
    logging.info('Verify the page heading')
    expect(page.get_by_role("heading", name=HEADING_NAME)).to_be_visible()

def test_navigate_to_community_page(page: Page):
    logging.info('Navigate to a page')
    page.goto(URL)
    logging.info('Navigate to Community')
    page.get_by_role("link", name=LINK_COMMUNITY).click()
    expect(page.get_by_role("heading", name=HEADING_WELCOME)).to_be_visible()
    logging.info('Navigate to Ambassadors page')
    page.get_by_role("link", name=LINK_AMBASSADOR).first.click()
    image_next_ambassador = page.get_by_role("img", name=AMBASSADOR_IMAGE_TEXT)
    expect(image_next_ambassador).to_be_visible()

def test_navigate_to_python_documentation(page: Page):
    logging.info('Navigate to a page')
    page.goto(URL)
    logging.info('Navigate to Docs')
    page.get_by_role("link", name=LINK_DOCS).click()
    expect(page.get_by_role("heading", name=HEADING_NAME)).to_be_visible()
    logging.info('Select Python from a drop-down list')
    dropdown = page.get_by_role("button", name=DOC_MENU_NAME)
    dropdown.hover(timeout=1000)
    dropdown.click()
    python_option = page.get_by_text(DOC_PYTHON_OPTION)
    python_option.click()
    doc_name = page.get_by_text(DOC_PYTHON_NAME)
    assert doc_name is not None

