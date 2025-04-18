import re
from playwright.sync_api import Page
import logging

# Logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
)

class PlaywrightPage:
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

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_page(self, url=URL):
        logging.info('Navigate to a page')
        self.page.goto(url)

    def return_page_title(self):
        return self.page.title()

    def click_on_link(self, link_name):
        logging.info('Click on a link')
        self.page.get_by_role("link", name=link_name).first.click()

    def is_heading_visible(self, heading_name):
        logging.info('Verify if a heading visible')
        return self.page.get_by_role("heading", name=heading_name).is_visible()

    def is_image_visible(self, image_name):
        logging.info('Verify if an image visible')
        return self.page.get_by_role("img", name=image_name).is_visible()

    def is_text_visible(self, text):
        logging.info('Verify if a text visible')
        return self.page.get_by_text(text).is_visible()

    def select_option_from_dropdown_menu(self, option_name, dropdown_menu):
        logging.info('Selecting an option from a dropdown menu')
        dropdown = self.page.get_by_role("button", name=dropdown_menu)
        dropdown.hover(timeout=1000)
        dropdown.click()
        python_option = self.page.get_by_text(option_name)
        python_option.click()




