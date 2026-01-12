# Bloggy Automation Test Suite

## Overview
This repository contains an automated test suite for the Bloggy fullstack blog application. The suite covers end-to-end scenarios using Playwright and Pytest, with support for multiple browsers and both headed/headless modes.

## Frameworks & Tools
- **Playwright**: For browser automation (Chromium, Firefox, WebKit)
- **Pytest**: For test execution and reporting
- **pytest-html**: For HTML test reports

## Why These Tools?
- **Playwright** provides fast, reliable, and cross-browser automation.
- **Pytest** is flexible, widely used, and integrates well with Playwright.
- **pytest-html** generates easy-to-share test reports.

## Setup Instructions
1. **Clone the repository:**
   ```sh
   git clone https://github.com/saikiranshet/maxhomeAiAutomation.git
   cd maxhomeAiAutomation
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   # Or
   source myenv/bin/activate  # On Mac/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install -r src/requirements.txt
   playwright install
   ```
4. **Set environment variables:**
   - Copy `.env.example` to `.env` and update values as needed (e.g., `LOCAL_SETUP_URL`).

## How to Run Tests
- **Default (headed, Chromium):**
  ```sh
  pytest src/tests/testLoginForAdmin.py --html=reports/report.html --self-contained-html
  ```
- **Headless mode:**
  ```sh
  pytest src/tests/testLoginForAdmin.py --headless --html=reports/report.html --self-contained-html
  ```
- **Different browsers:**
  ```sh
  pytest src/tests/testLoginForAdmin.py --browser=firefox
  pytest src/tests/testLoginForAdmin.py --browser=webkit
  ```
- **Clean reports before running:**
  ```sh
  python src/utils/clean_reports.py && pytest ...
  ```

## Test Coverage Summary
- Blog management (create, delete)
- Public blog viewing (list, search, view, theme persistence, read status)
- Pagination (navigation, URL state)
- Admin login and protected routes

## Test Report
- After running tests, open `reports/report.html` in your browser to view results.

## Assumptions & Notes
- The backend and frontend servers must be running before tests.
- Test data is reset using `npm run reset && npm run seed`.
- Locators and test data are based on the provided application structure.

## Questions?
See ASSIGNMENT.md or contact the maintainer.
