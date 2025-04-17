from playwright.sync_api import Page, expect
import logging
import pytest
from POM.playwrightPOM import PlaywrightPage

# Logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
)

def test_page_has_correct_title(page: Page):
    pagePOM = PlaywrightPage(page)
    logging.info('Navigate to a page')
    pagePOM.navigate_to_page()
    logging.info('Verify the page title')
    page_title = pagePOM.return_page_title()
    assert pagePOM.PAGE_TITLE in page_title

def test_verify_link_is_displayed(page: Page):
    pagePOM = PlaywrightPage(page)
    logging.info('Navigate to a page')
    pagePOM.navigate_to_page()
    logging.info('Click on Get Started')
    pagePOM.click_on_link(pagePOM.LINK_NAME)
    logging.info('Verify the page heading')
    assert pagePOM.is_heading_visible(pagePOM.HEADING_NAME) == True

def test_navigate_to_community_page(page: Page):
    pagePOM = PlaywrightPage(page)
    logging.info('Navigate to a page')
    pagePOM.navigate_to_page()
    logging.info('Navigate to Community')
    pagePOM.click_on_link(pagePOM.LINK_COMMUNITY)
    assert pagePOM.is_heading_visible(pagePOM.HEADING_WELCOME) is not None
    logging.info('Navigate to Ambassadors page')
    pagePOM.click_on_link(pagePOM.LINK_AMBASSADOR)
    page.screenshot(path="screenshot1.png", full_page=True)
    assert pagePOM.is_image_visible(pagePOM.AMBASSADOR_IMAGE_TEXT) == True

def test_navigate_to_python_documentation(page: Page):
    pagePOM = PlaywrightPage(page)
    logging.info('Navigate to a page')
    pagePOM.navigate_to_page()
    logging.info('Navigate to Docs')
    pagePOM.click_on_link(pagePOM.LINK_DOCS)
    assert pagePOM.is_heading_visible(pagePOM.HEADING_NAME) is not None
    logging.info('Select Python from a drop-down list')
    pagePOM.select_option_from_dropdown_menu(pagePOM.DOC_PYTHON_OPTION, pagePOM.DOC_MENU_NAME)
    page.screenshot(path="screenshot2.png", full_page=True)
    assert pagePOM.is_text_visible(pagePOM.DOC_PYTHON_NAME) is not None

