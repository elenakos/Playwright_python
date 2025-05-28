'''
Navigate to TODOS page
Add to a list
Remove from a list
Filter
'''

from playwright.sync_api import Page, expect

# Variables
# -------------------------------
URL = "https://demo.playwright.dev/todomvc/#/"

# Test cases
# -------------------------------
def test_add_todo_item(page: Page):
    print("Verifying that a new todo item can be added")
    todo_item_to_add = "Item One"
    assert navigate_to_todos(page), "The page did not appear"
    assert verify_text_on_page(page, HEADER_NAME), "TODOS test did nto appear"
    add_todo_item(page, todo_item_to_add)
    assert verify_todo_item_is_present(page, todo_item_to_add), "TO-DO item was not added"

def test_todo_item_can_be_marked_as_done(page: Page) :
    print("Verifying that a todo item can be marked as done")
    todo_item_to_add = "Item To Mark"
    assert navigate_to_todos(page), "The page did not appear"
    assert verify_text_on_page(page, HEADER_NAME), "TODOS test did nto appear"
    add_todo_item(page, todo_item_to_add)
    assert verify_todo_item_is_present(page, todo_item_to_add), "TO-DO item was not added"
    assert mark_todo_item_as_done(page, todo_item_to_add), "TO-DO item checkbox was not checked"

def test_todo_item_can_be_deleted(page: Page):
    print("Verifying that a todo item can be deleted")
    todo_item_to_delete = "Item To Delete"
    assert navigate_to_todos(page), "The page did not appear"
    assert verify_text_on_page(page, HEADER_NAME), "TODOS test did nto appear"
    add_todo_item(page, todo_item_to_delete)
    assert verify_todo_item_is_present(page, todo_item_to_delete), "TO-DO item was not added"
    delete_todo_item(page, todo_item_to_delete)
    assert not verify_todo_item_is_present(page, todo_item_to_delete), "TO-DO item was not deleted"

def test_todo_items_can_be_filtered_by_active(page: Page):
    print("Verifying that items can be filtered")


# Elements - labels/ids
# -------------------------------
HEADER_NAME = "todos"
TODO_INPUT_FIELD_PLACEHOLDER = "What needs to be done?"
TODO_CHECKBOX = "Toggle Todo"
DELETE_BUTTON = "Delete"
ALL_FILTER_LINK = "All"
ACTIVE_FILTER_LINK = "Active"
COMPLETED_FILTER_LINK = "Completed"
TODO_CELL = "todo-title"

# Elements - methods
# -------------------------------
def return_todo_input(page: Page):
    return page.get_by_placeholder(TODO_INPUT_FIELD_PLACEHOLDER)

def return_todo_element(page: Page, todo_item):
    return page.get_by_role("listitem").filter(has_text=todo_item)

def return_todo_element_checkbox(page: Page, todo_item):
    return page.get_by_role("listitem").filter(has_text=todo_item).get_by_label(TODO_CHECKBOX)

def return_todo_delete_button(page: Page, todo_item):
    return page.get_by_role("listitem").filter(has_text=todo_item).get_by_label(DELETE_BUTTON)

# Methods
# -------------------------------
def navigate_to_todos(page: Page):
    print("Navigate to TODOS")
    page.goto(URL)
    element = return_todo_input(page)
    expect(element).to_be_visible(timeout=10000)
    return True

def verify_text_on_page(page: Page, text_to_verify: str):
    print("Verify this text on page: " + text_to_verify)
    content = page.locator("body").text_content()
    if text_to_verify in content:
        print("--> Text found!")
        return True
    else:
        print("--> Text not found!")
        return False

def add_todo_item(page: Page, todo_item):
    print("Add this todo item: {}".format(todo_item))
    element = return_todo_input(page)
    element.type(todo_item)
    element.press("Enter")

def verify_todo_item_is_present(page: Page, todo_item):
    print("Check if a todo item is present")
    element = return_todo_element(page, todo_item)
    if element:
        print("--> TO-DO item found!")
        return True
    else:
        print("--> TO-DO item was not found!")
        return False

def mark_todo_item_as_done(page: Page, todo_item):
    print("Mark this item as done: {}".format(todo_item))
    element = return_todo_element_checkbox(page, todo_item)
    if element:
        print("--> TO-DO item checkbox is found!")
        element.click()
        return True
    else:
        print("--> TO-DO item checkbox is not found!")
        return False

def verify_todo_item_is_checked(page: Page, todo_item):
    print("Verify that the checkbox is clicked")
    element = return_todo_element_checkbox(page, todo_item)
    if element.is_checked():
        print("--> TO-DO item checkbox is checked!")
        return True
    else:
        print("--> TO-DO item checkbox is not checked!")
        return False

def delete_todo_item(page: Page, todo_item):
    print("Delete this item: {}".format(todo_item))
    todo_element = return_todo_element(page, todo_item)
    todo_element.hover()
    element = return_todo_delete_button(page, todo_item)
    if element:
        print("--> TO-DO item delete button is found!")
        element.click()
        return True
    else:
        print("--> TO-DO item delete button is not found!")
        return False