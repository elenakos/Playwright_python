
from playwright.sync_api import Playwright, defineConfig, devices

def config(playwright: Playwright):
    return {
        "testDir": "./Tests", # Directory containing test files
        "timeout": 30000,     # Timeout for tests in milliseconds
        "workers": 2,         # Number of parallel workers
        "reporter": "html",   # Reporter to use (e.g., "list", "html")
        "use": {
            "headless": True, # Whether to run in headless mode
            "browserName": "chromium", # Default browser to use
        },
        "projects": [
            {
                "name": "chromium",
                "use": {
                    "browserName": "chromium",
                },
            },
            {
                "name": "firefox",
                "use": {
                    "browserName": "firefox",
                },
            },
             {
                "name": "webkit",
                "use": {
                    "browserName": "webkit",
                },
            }
        ]
    }

playwright_config = defineConfig(config)