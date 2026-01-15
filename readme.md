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

## How to Run Tests

### Run All Tests
- **Default (headed, Chromium):**
  ```sh
  python -m pytest tests/ --html=reports/report.html --self-contained-html
  ```
- **Headless mode:**
  ```sh
  python -m pytest tests/ --headless --html=reports/report.html --self-contained-html
  ```
- **Different browsers:**
  ```sh
  python -m pytest tests/ --browser=firefox
  python -m pytest tests/ --browser=webkit
  ```

### Run Specific Test Suites
- **Admin Login Tests:**
  ```sh
  pytest tests/testLoginForAdmin.py --html=reports/report.html --self-contained-html
  ```

### Run Specific Test Cases
- **Run a single test:**
  ```sh
  pytest tests/test_blog_management.py::TestBlogManagement::test_BLOG_MGMT_01_create_and_publish_blog
  ```

### Clean Reports Before Running
  ```sh
  python src/utils/clean_reports.py && pytest tests/ --html=reports/report.html --self-contained-html
  ```

## Test Coverage Summary

### Test Files Structure
- **`tests/test_blog_management.py`**: Blog Management test suite
  - `test_BLOG_MGMT_01_create_and_publish_blog`: Create a new blog post and publish it
  - `test_BLOG_MGMT_02_delete_blog_with_confirmation`: Delete a blog post with confirmation
  - `test_BLOG_MGMT_03_delete_blog_cancel_confirmation`: Cancel blog deletion (negative test)

- **`tests/test_public_blog_viewing.py`**: Public Blog Viewing test suite
  - `test_PUBLIC_VIEW_01_view_list_of_published_blogs`: View list of published blogs
  - `test_PUBLIC_VIEW_02_search_blogs_by_keyword`: Search for blogs by keyword
  - `test_PUBLIC_VIEW_03_view_a_blog`: View a blog post detail page
  - `test_PUBLIC_VIEW_04_theme_preference_persists_across_sessions`: Theme preference persistence
  - `test_PUBLIC_VIEW_05_read_blogs_visually_marked_across_sessions`: Read status persistence

- **`tests/test_pagination.py`**: Pagination test suite
  - `test_PAGINATION_01_navigate_through_multiple_pages`: Navigate through multiple pages
  - `test_PAGINATION_02_page_state_persists_in_url`: Page state persists in URL
  - `test_PAGINATION_03_navigate_to_specific_page`: Navigate to a specific page number

- **`tests/testLoginForAdmin.py`**: Admin Login test suite
  - `test_ADM_LOGIN_01`: Valid admin login
  - `test_ADM_LOGIN_02`: Invalid credentials login

### Page Object Models (POM)
- **`POM/login.py`**: Login page interactions
- **`POM/adminBlogPage.py`**: Admin blog management operations
- **`POM/publicBlogPage.py`**: Public blog viewing operations

### Coverage Areas
- ✅ Blog management (create, publish, delete with confirmation)
- ✅ Public blog viewing (list, search, view, theme persistence, read status)
- ✅ Admin login and protected routes

## Test Report
- After running tests, open `reports/report.html` in your browser to view results.

## CI/CD Integration
- (Optional) Add a `.github/workflows/ci.yml` for GitHub Actions to run tests on every push.

## Assumptions & Notes
- The backend and frontend servers must be running before tests.
- Test data is reset using `npm run reset && npm run seed`.
- Locators and test data are based on the provided application structure.

## Questions?
- See ASSIGNMENT.md or contact the maintainer.
