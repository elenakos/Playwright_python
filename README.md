[Playwright](https://playwright.dev/) is a powerful open-source automation tool developed by Microsoft. It's primarily used for end-to-end testing of web applications, and it can be used with many languages. 

This repository includes examples of using Playwright's [Python](https://github.com/microsoft/playwright-python) implementation.

This project incorporates a basic GitHub Actions integration, with detailed configuration provided at the end of this document.

# How to start with Playwright with python binding

1. Install the Pytest plugin:
```
pip install pytest-playwright
```

2. Install the required browsers:
```
playwright install
```
3. Create a new python project in any IDE of you choice. This project was created in PyCharm.
4. Start creating test suites and Page Object Model (POM) classes.  


# How to work with different UI elements
UI automation testing rely on well-defined elements in applications. Playwright offers multiple ways to identify elements through [locators](https://playwright.dev/python/docs/locators) such as 
`page.get_by_role()`, `page.get_by_text()`, etc .

# How verification works
Each automation test case should have at least one verification point. Playwright offers multiple verifications or [assertions](https://playwright.dev/python/docs/test-assertions) such as `expect(locator).to_be_checked()`, 
`expect(locator).to_be_enabled()`, `expect(locator).to_have_text()`, etc.

If pytest is used in your test automation framework, leverage its built-in `assert` functionality.

# Debugging with Playwright Inspector 
To debug a specific test case with the inspector:
```
PWDEBUG=1 pytest -s -k test_case_name
```
You will be able to execute scripts line-by-line, inspect elements, etc:
![img.png](img.png)

# How to Execute Playwright tests
To run all tests in a headless mode without showing a browser, open a terminal and type:
```
pytest
```

To run all tests in a headed mode, open a terminal and type:
```
pytest --headed
```

To generate reports, install `pip install pytest-html` and use `--html` option while running scripts: 
```
pytest --html=Results/verify.html Tests/test_verify_page_elements.py
```
![img_1.png](img_1.png)

# Integration with GitHub Actions
This project uses GitHub Actions to automatically run all tests with any code updates. The configuration defined in `.github/workflows/playwright.yml`
