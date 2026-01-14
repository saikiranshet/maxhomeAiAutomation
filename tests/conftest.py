import pytest
from playwright.sync_api import sync_playwright
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
# api_key = os.getenv("API_KEY")

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode (default: headed)"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        choices=["chromium", "firefox", "webkit"],
        help="Browser to use: chromium, firefox, or webkit (default: chromium)"
    )

@pytest.fixture(scope="session")
def setupcheck(request):
    """Set up a single browser and page for the entire test session.

    This keeps the same logged-in session active across all tests that use
    this fixture, until the full pytest run is completed.
    """
    url = os.getenv("LOCAL_SETUP_URL")
    print(f"Testing URL: {url}")
    headless = request.config.getoption("--headless")
    browser_name = request.config.getoption("--browser")
    with sync_playwright() as p:
        browser_launcher = getattr(p, browser_name)
        browser = browser_launcher.launch(
            headless=headless,
            args=["--start-maximized", "--window-size=1920,1080"]  # Ensure full-screen
        )
        page = browser.new_page(viewport=None)  # No viewport restriction
        page.goto(url)
        time.sleep(10)
        yield page
        browser.close()
        
        
def pytest_sessionstart(session):
    # Clean reports before tests
    from utils.clean_reports import clean_reports_folder
    clean_reports_folder()