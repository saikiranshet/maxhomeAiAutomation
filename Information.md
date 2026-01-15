# Bloggy Automation - Quick Reference Guide

## 📖 Framework Overview

A **Playwright + Pytest** automation framework for the Bloggy blog application, using the **Page Object Model (POM)** design pattern.

---

## 🏗️ Architecture & Design Patterns

### 1. Page Object Model (POM)
- **Separates page interactions from test logic** - Tests focus on business scenarios, not implementation details
- **`POM/login.py`** contains reusable methods for page actions
- **Locators are stored separately** in `locators/` for maintainability
- **Single source of truth** for page elements and actions

### 2. Directory Structure
```
maxhomeAiAutomation/
├── data/
│   └── config.yaml              # Test data (credentials)
├── locators/
│   └── loginPageLocators.py     # XPath/CSS selectors
├── POM/
│   └── login.py                 # Page object with business logic
├── tests/
│   ├── conftest.py              # Pytest fixtures & configuration
│   ├── testLoginForAdmin.py     # Admin login tests
│   └── testblogging.py          # Blog management tests
├── utils/
│   └── clean_reports.py         # Utility to clean old reports
└── reports/
    └── report.html              # Generated test reports
```

---

## 🔧 Components

### 1. Test Configuration (`pytest.ini`)
- **Test discovery**: Automatically finds `test*.py` files in `tests/` directory
- **HTML reports**: Generates self-contained HTML reports
- **Markers**: `blog_management`, `public_viewing`, `pagination`, `admin`, `public`
- **Logging**: CLI logging with timestamps and formatted output

### 2. Fixtures (`conftest.py`)
**`setupcheck` - Session-scoped fixture:**
- Launches browser (Chromium/Firefox/WebKit)
- Supports headed/headless mode via `--headless` flag
- Loads URL from `.env` file (`LOCAL_SETUP_URL`)
- **Reuses the same browser session** across all tests for efficiency

**Command-line options:**
- `--headless`: Run browser without UI
- `--browser`: Choose browser (chromium/firefox/webkit)

### 3. Page Object (`POM/login.py`)
Contains reusable methods for:

**Authentication:**
- `login_user()` - Valid admin login
- `login_user_with_invalid_creds()` - Invalid credentials test

**Blog Management:**
- `login_user_for_blog()` - Create and publish blog
- `verify_title_to_be_available_in_dashboard()` - Verify blog creation
- `click_delete_icon_for_blog()` - Delete blog functionality

**Public Viewing:**
- `search_screen()` - Search functionality
- `switch_to_dark_mode()` - Theme switching
- `click_readmore_button()` - Read more action

**Assertions:**
- `verify_no_blogs_found()` - Search validation
- `verify_dark_mode_active()` - Theme persistence check

### 4. Locators (`locators/loginPageLocators.py`)
- **Centralized XPath selectors** - All element locators in one place
- **Easy to update** when UI changes
- **Examples**: `ADMIN_BUTTON`, `USERNAME_FIELD`, `DELETE_ICON`, `BLOG_CARD_TITLE`

### 5. Test Data (`data/config.yaml`)
- **Credentials stored in YAML** format
- **Separates data from code** - Easy to update without code changes
- Contains admin credentials and invalid test data

---

## 📊 Test Coverage

### Admin Login (`testLoginForAdmin.py`)
- **`test_ADM_LOGIN_01`**: Valid admin login and logout
- **`test_ADM_LOGIN_02`**: Invalid credentials validation

### Blog Management (`testblogging.py`)
- **`test_blogmgmt_001`**: Create and publish blog post
- **`test_blogmgmt_002`**: Validation test (empty title prevents publishing)
- **`test_blogmgmt_003`**: Delete blog post
- **`test_blogmgmt_004`**: Cancel blog deletion
- **`test_publicviewing_005`**: Search with no results
- **`test_publicviewing_006`**: Search with results
- **`test_publicviewing_007`**: Dark mode persistence across page reloads
- **`test_publicviewing_008`**: Read more functionality

---

## ✨ Key Features

1. **Cross-browser Testing**: Supports Chromium, Firefox, and WebKit
2. **Headed/Headless Execution**: Run with or without browser UI
3. **HTML Reports**: Self-contained HTML reports for easy sharing
4. **Session Reuse**: Single browser session across tests for efficiency
5. **Environment Variables**: `.env` file for configuration management
6. **Auto-cleanup**: Automatically cleans old reports before test runs

---

## 🔄 How It Works

1. **Test execution starts** → `conftest.py` runs
2. **`setupcheck` fixture** launches browser and navigates to application URL
3. **Tests use `LoginPage` object** to interact with pages
4. **`LoginPage` uses locators** from `loginPageLocators.py`
5. **Test data** comes from `config.yaml`
6. **Results generate** HTML report in `reports/` directory

---

## 🎯 Best Practices Implemented

✅ **Separation of Concerns**: POM, locators, tests, and data are separated  
✅ **Reusability**: Shared methods in Page Objects reduce code duplication  
✅ **Maintainability**: Centralized locators make updates easy  
✅ **Configuration**: Externalized test data and environment variables  
✅ **Reporting**: HTML reports provide detailed test execution results  

This structure supports **scalable, maintainable test automation** that can grow with your application.

---

## 🚀 Quick Start Commands

### Essential Commands
```bash
# Activate virtual environment (Windows)
myenv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt
playwright install

# Run all tests (default)
pytest tests/

# Run all tests with HTML report
pytest tests/ --html=reports/report.html --self-contained-html

# Run in headless mode
pytest tests/ --headless

# Run with specific browser
pytest tests/ --browser=firefox
pytest tests/ --browser=webkit
```

## 📋 Test Execution Quick Reference

### Run Specific Test Files
```bash
# Admin login tests
pytest tests/testLoginForAdmin.py

# Blog management tests
pytest tests/testblogging.py

# Both test files
pytest tests/testLoginForAdmin.py tests/testblogging.py
```

### Run Specific Test Functions
```bash
# Run single test by name
pytest tests/testLoginForAdmin.py::test_ADM_LOGIN_01

# Run single test with verbose output
pytest tests/testblogging.py::test_blogmgmt_001 -v

# Run tests matching pattern
pytest -k "login" tests/
pytest -k "blog" tests/
```

### Advanced Options
```bash
# Run with markers (if configured)
pytest -m admin tests/
pytest -m "blog_management" tests/

# Run with detailed output
pytest tests/ -v -s

# Stop on first failure
pytest tests/ -x

# Run last failed tests only
pytest --lf tests/

# Run with parallel execution (if pytest-xdist installed)
pytest tests/ -n auto
```

## 🔧 Configuration Files

### Environment Setup
Create a `.env` file in the project root:
```env
LOCAL_SETUP_URL=http://localhost:3000
# Add other environment variables as needed
```

### Test Data Configuration
Edit `data/config.yaml` to update test credentials:
```yaml
credentials:
  adminusername: "admin"
  password: "admin123"
  invalid_username: "wrongpass"
  invalid_password: "wronguser"
```

## 🐛 Troubleshooting

### Common Issues

#### 1. Browser Not Found
```bash
# Solution: Install Playwright browsers
playwright install
playwright install chromium  # For specific browser
```

#### 2. Module Not Found Errors
```bash
# Solution: Ensure virtual environment is activated and dependencies installed
pip install -r requirements.txt
```

#### 3. Tests Failing - Application Not Running
- **Issue**: Tests fail with connection errors
- **Solution**: Ensure the Bloggy application is running before executing tests
- **Check**: Verify `LOCAL_SETUP_URL` in `.env` file points to correct URL

#### 4. Locator Not Found Errors
- **Issue**: `Element not found` or `Timeout` errors
- **Solution**: 
  - Check if UI has changed
  - Update locators in `locators/loginPageLocators.py`
  - Increase wait timeouts if needed

#### 5. Report Generation Issues
```bash
# Clean old reports and regenerate
python utils/clean_reports.py
pytest tests/ --html=reports/report.html --self-contained-html
```

#### 6. Import Errors
- **Issue**: `ModuleNotFoundError` when running tests
- **Solution**: Ensure you're running from project root directory
- **Check**: Verify `sys.path.append` in conftest.py is correct

## 📁 Project Structure Quick Reference

```
maxhomeAiAutomation/
├── data/
│   └── config.yaml              # Test credentials & data
├── locators/
│   └── loginPageLocators.py     # All XPath/CSS selectors
├── POM/
│   └── login.py                 # Page Object Model methods
├── tests/
│   ├── conftest.py              # Pytest fixtures & setup
│   ├── testLoginForAdmin.py     # Admin login test cases
│   └── testblogging.py          # Blog management test cases
├── utils/
│   └── clean_reports.py         # Report cleanup utility
├── reports/
│   └── report.html              # Generated test reports
├── pytest.ini                   # Pytest configuration
├── requirements.txt             # Python dependencies
└── .env                         # Environment variables (create this)
```

## 🎯 Test Cases Quick Reference

### Admin Login Tests (`testLoginForAdmin.py`)
- `test_ADM_LOGIN_01`: Valid admin login and logout
- `test_ADM_LOGIN_02`: Invalid credentials validation

### Blog Management Tests (`testblogging.py`)
- `test_blogmgmt_001`: Create and publish blog post
- `test_blogmgmt_002`: Validation test (empty title)
- `test_blogmgmt_003`: Delete blog post
- `test_blogmgmt_004`: Cancel blog deletion
- `test_publicviewing_005`: Search with no results
- `test_publicviewing_006`: Search with results
- `test_publicviewing_007`: Dark mode persistence
- `test_publicviewing_008`: Read more functionality

## 🔍 Debugging Tips

### Enable Debug Mode
```bash
# Run with maximum verbosity
pytest tests/ -v -s --tb=long

# Run with Playwright debug mode
PWDEBUG=1 pytest tests/
```

### View Test Execution
- Use `--headless=false` (default) to see browser actions
- Add `time.sleep()` in Page Object methods for debugging
- Use `page.screenshot()` to capture screenshots on failures

### Check Logs
- Pytest logs are displayed in console (configured in `pytest.ini`)
- HTML report contains detailed failure information
- Check `reports/report.html` for test execution details

## 📝 Adding New Tests

### Step 1: Add Locators
Edit `locators/loginPageLocators.py`:
```python
class LoginPageLocators:
    NEW_ELEMENT = "//xpath/to/element"
```

### Step 2: Add Page Object Methods
Edit `POM/login.py`:
```python
def new_action(self):
    self.new_element.click()
    # Add your logic here
```

### Step 3: Create Test Case
Create or edit test file in `tests/`:
```python
def test_new_feature(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    login_page.new_action()
    # Add assertions
```

## 🔄 Best Practices

1. **Always use Page Object Model**: Don't write locators directly in tests
2. **Use meaningful test names**: Follow naming convention `test_FEATURE_##_description`
3. **Keep tests independent**: Each test should be able to run standalone
4. **Use fixtures**: Leverage `setupcheck` fixture for browser setup
5. **Update locators**: Keep locators updated when UI changes
6. **Clean reports**: Run cleanup utility before generating new reports

## 📊 Viewing Test Reports

### HTML Report
```bash
# Generate report
pytest tests/ --html=reports/report.html --self-contained-html

# Open report (Windows)
start reports/report.html

# Open report (Mac)
open reports/report.html

# Open report (Linux)
xdg-open reports/report.html
```

## 🛠️ Maintenance

### Update Dependencies
```bash
pip install --upgrade -r requirements.txt
playwright install --force
```

### Clean Project
```bash
# Remove Python cache
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Clean reports
python utils/clean_reports.py
```

## 📞 Support

For issues or questions:
- Check the main `readme.md` for detailed documentation
- Review test code in `tests/` directory
- Check `pytest.ini` for configuration options
- Verify `.env` file is properly configured

---

**Note**: This is a quick reference guide. For detailed documentation, see `readme.md`.
