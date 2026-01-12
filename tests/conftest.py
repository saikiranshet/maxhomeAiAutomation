
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from dotenv import load_dotenv
from POM.login import LoginPage
from playwright.sync_api import sync_playwright
import time


# Load .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("API_KEY")

print(f"API Key: {api_key}")


# def pytest_addoption(parser):
#     """Add a command-line option for running tests in headless mode."""
#     parser.addoption("--headless", action="store_true", default=True, help="Run browser in headless mode")


@pytest.fixture(scope="session")
def setupcheck():
    """Set up the browser and page for all tests in the session."""
    url = os.getenv("LOCAL_SETUP_URL")
    print(f"Testing URL: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized", "--window-size=1920,1080"]  # Ensure full-screen
        )
        page = browser.new_page(viewport=None)  # No viewport restriction
        page.goto(url)
        time.sleep(10)
        yield page
        browser.close()
