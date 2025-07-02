'''
Open Chrom
Use .on method for request and response
Open page
print url, statuses
'''
import asyncio
from pydoc import allmethods

from playwright.async_api import async_playwright

# Variables
# -------------------------------
URL = "https://google.com"

# Test cases
# -------------------------------

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Lists to store captured requests and responses
        all_requests = []
        all_responses = []


        # Define the event handler functions
        def handle_request(request):
            all_requests.append(request)
            #print(f"Request URL: {request.url}")
            #print(f"Request Method: {request.method}")
            #print(f"Request Resource Type: {request.resource_type}")

        def handle_response(response):
            all_responses.append(response)
            #print(f"Response URL: {response.url}")
            #print(f"Response Status: {response.status}")
            #print(f"Response Headers: {response.headers}")

        # Register the event handlers
        page.on("request", handle_request)
        page.on("response", handle_response)

        # Navigate to a page that makes network requests
        print(f"Navigating to {URL}...")
        await page.goto(URL)
        print("Navigation complete.")
        await browser.close()
        print("\n--------- Requests --------")
        print(f"Number of captured requests: {len(all_requests)}")
        print(f"URL: {all_requests[0].url}")
        print(f"Method: {all_requests[0].method}")
        print("\n---------- Responses-------")
        print(f"Number of captured responses: {len(all_responses)}")
        print(f"Requests: {all_responses[0].url}")
        print(f"Request: {all_responses[0].request}")
        print("\n----------- End -----------")

if __name__ == "__main__":
    asyncio.run(main())