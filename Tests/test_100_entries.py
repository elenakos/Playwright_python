
'''
In this example, the script goes to [Hacker News/newest](https://news.ycombinator.com/newest)
and validates that EXACTLY the first 100 articles are sorted from newest to oldest
'''

import re
from playwright.sync_api import Page, expect

# Variables
URL = "https://news.ycombinator.com/newest"
PAGE_TITLE = "Hacker News"
MORE_BUTTON_LINK = "More"


def test_navigate_to_news(page: Page):
    page.goto(URL)
    expect(page).to_have_title(re.compile(PAGE_TITLE))

    # Save all titles with dates
    timestamps = capture_timestamps(page, 100)
    print(timestamps)

    # Check if all dates are in order
    if verify_datestamps_order(timestamps):
        print("All dates are in the correct order")
    else:
        print("Dates are not in the correct order")


def capture_timestamps(page: Page, number_of_articles: int):
    print("Capture timestamps")
    timestamps = []
    counter = 0
    while counter < number_of_articles:
        elements = []
        elements = page.locator('span.age').all()
        for element in elements:
            title = element.get_attribute('title')
            if title:
                # Dates are presented in this format
                # '2025-03-19T21:07:13 1742418433'
                # So let's save an epoch-based time
                epoch_time = title.split(" ")[1]
                timestamps.append(epoch_time)
                counter += 1
                if counter > 100:
                    break
        print("Go to the next page")
        more_link = page.get_by_role("link", name=MORE_BUTTON_LINK, exact=True)
        more_link.click()
    return timestamps

def verify_datestamps_order(array):
    print("Verify that all datestamps are sorted from newest to oldest")
    # All dates will be in this format:'1742418433'
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            return False
    return True

