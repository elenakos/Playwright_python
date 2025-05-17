'''
Navigate to http://eng-qa-interview.s3-website-us-east-1.amazonaws.com/
Scroll dynamically to the N-th item
Add any test comment
Verify that the comment was saved
'''
import time
from playwright.sync_api import Page, expect

# Variables
URL = "http://eng-qa-interview.s3-website-us-east-1.amazonaws.com/"
PAGE_NAME = "Movie List"
DETAILS_BUTTON = "Details"
DETAILS_LINK = "/movie/"
DELETE_BUTTON = "Delete"
BUTTON_ADD_COMMENT = "Add Comment"

def test_add_comments_to_15th_movie_and_verify(page: Page):
    item_number = 15
    comment_text = "Hello World - " + str(item_number)
    print("Add and verify comments to {} item".format(item_number))
    assert navigate_to_page(page), "Page did not load"
    assert verify_text_on_page(page, PAGE_NAME), PAGE_NAME + " text is not on page"
    assert select_nth_movie(page, item_number), "The movie was not selected"
    add_comments(page, comment_text)
    assert verify_text_on_page(page, comment_text), "Comments were not added/saved"

def test_add_comments_to_300th_movie_and_verify(page: Page):
    item_number = 300
    comment_text = "Hello World again - " + str(item_number)
    print("Add and verify comments to {} item".format(item_number))
    assert navigate_to_page(page), "Page did not load"
    assert verify_text_on_page(page, PAGE_NAME), PAGE_NAME + " text is not on page"
    assert select_nth_movie(page, item_number), "The movie was not selected"
    add_comments(page, comment_text)
    assert verify_text_on_page(page, comment_text), "Comments were not added/saved"

def navigate_to_page(page: Page):
    print("Navigate to the main page")
    page.goto(URL)
    # wait until a table appears
    element = page.get_by_role("cell", name="Title", exact=True)
    expect(element).to_be_visible(timeout=10000)
    return True

def select_nth_movie(page: Page, item_number: int):
    print("Selecting {}-th movie".format(item_number))
    # Get all Details buttons
    element_to_wait = element = page.get_by_role("button", name=DETAILS_BUTTON, exact=True).first
    expect(element_to_wait).to_be_visible(timeout=10000)
    elements = page.locator("button").filter(has_text=DETAILS_BUTTON)
    # Find the number of elements
    if elements.count() < item_number:
        # Keep scrolling and checking until the number of elements on a screen is > than a needed element index
        # But do not scroll more than 5 times
        count = 1
        while True:
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            elements = page.locator("button").filter(has_text=DETAILS_BUTTON)
            if elements.count() > item_number:
                break
            count += 1
            if count > 5:
                print("Can't select {} movie - only {} movies are present".format(item_number, elements.count()))
                return False
    button_to_click = elements.nth(item_number-1)
    button_to_click.scroll_into_view_if_needed(timeout=1000)
    button_to_click.click()
    return True

def add_comments(page: Page, comment_text: str):
    print("Adding comments to page: {}".format(comment_text))
    element = page.get_by_role("textbox")
    element.clear()
    element.type(comment_text)
    add_comment_button = page.get_by_role("button", name=BUTTON_ADD_COMMENT)
    add_comment_button.click()

def verify_text_on_page(page: Page, text_to_verify: str):
    print("Verify this text on the page: {}".format(text_to_verify))
    content = page.locator("body").text_content()
    if text_to_verify in content:
        print("--> Text found!")
        return True
    else:
        print("--> Text not found!")
        return False



