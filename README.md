This repo contains sample test written in [Playwright-python](https://github.com/microsoft/playwright-python).

## How to Setup Playwright

Install the Pytest plugin:
```
pip install pytest-playwright
```

Install the required browsers:
```
playwright install
```

## How to Execute Playwright tests
To run all tests in a headless mode without showing a browser, open a terminal and type:
```
pytest
```

To run all tests in a headed mode, open a terminal and type:
```
pytest --headed
```

## Debugging with Playwright Inspector 
To debug a specific test case with the inspector:
```
PWDEBUG=1 pytest -s -k test_case_name
```

![img.png](img.png)