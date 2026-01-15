
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import random
import time
from playwright.sync_api import Page
from locators.loginPageLocators import LoginPageLocators
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of login.py
CONFIG_PATH = os.path.join(BASE_DIR, "..", "data", "config.yaml")  # Navigate to data/config.yaml

# Load YAML configuration
with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file) 

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_button = page.locator(LoginPageLocators.ADMIN_BUTTON)
        self.username_field = page.locator(LoginPageLocators.USERNAME_FIELD)
        self.password_field = page.locator(LoginPageLocators.PASSWORD_FIELD)
        self.submit_button = page.locator(LoginPageLocators.SUBMIT_BUTTON)
        self.logout_button = page.locator(LoginPageLocators.LOGOUT)
        self.blog_post_button = page.locator(LoginPageLocators.BLOG_POST_BUTTON)
        self.title_check = page.locator(LoginPageLocators.TITLE_CHECK).first
        self.excerpt_check = page.locator(LoginPageLocators.EXCERPT_CHECK)
        self.content_check = page.locator(LoginPageLocators.CONTENT_CHECK)
        self.category_check = page.locator(LoginPageLocators.CATEGORY_CHECK)
        self.category_option = page.locator(LoginPageLocators.CATEGORY_OPTION)
        self.tags_check = page.locator(LoginPageLocators.TAGS_CHECK)
        self.tags_check_option_1 = page.locator(LoginPageLocators.TAGS_CHECK_OPTION_1)
        self.tags_check_option_2 = page.locator(LoginPageLocators.TAGS_CHECK_OPTION_2)
        self.tags_check_option_3 = page.locator(LoginPageLocators.TAGS_CHECK_OPTION_3)
        self.tags_check_option_4 = page.locator(LoginPageLocators.TAGS_CHECK_OPTION_4)
        self.publish_now_button = page.locator(LoginPageLocators.PUBLISH_NOW_BUTTON)
        self.save_button = page.locator(LoginPageLocators.SAVE_BUTTON)
        self.cancel_button = page.locator(LoginPageLocators.CANCEL_BUTTON)
        self.content_click = page.locator(LoginPageLocators.CONTENT_CLICK)
        self.test_title_created_check = page.locator(LoginPageLocators.TEST_TITLE_CREATED)
        self.delete_icon = page.locator(LoginPageLocators.DELETE_ICON)
        self.delete_button = page.locator(LoginPageLocators.DELETE_BUTTON)
        self.confirm_delete_button = page.locator(LoginPageLocators.CONFIRM_DELETE_BUTTON)
        self.cancel_delete_button = page.locator(LoginPageLocators.CANCEL_DELETE_BUTTON)
        self.home_button = page.locator(LoginPageLocators.HOME_BUTTON)
        self.search_input = page.locator(LoginPageLocators.SEARCH_INPUT)
        self.search_button = page.locator(LoginPageLocators.SEARCH_BUTTON)
        self.no_blogs_found = page.locator(LoginPageLocators.NO_BLOGS_FOUND)
        self.blog_card = page.locator(LoginPageLocators.BLOG_CARD)
        self.blog_card_title = page.locator(LoginPageLocators.BLOG_CARD_TITLE)
        self.switch_to_dark_mode = page.locator(LoginPageLocators.SWITCH_TO_DARK_MODE)
        
    def home_screen(self):
        self.home_button.click()
        self.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(1)
    
    def reload_page(self):
        self.page.reload()
        self.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(1)
    
    def switch_to_dark_mode(self):
        self.switch_to_dark_mode.click()
        self.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(1)
    
    def verify_dark_mode_active(self):
        time.sleep(1)
        body_class = self.page.locator("body").get_attribute("class") or ""
        assert "dark" in body_class.lower(), "Dark mode should be active"
       
    def search_screen(self, search_term="Saikiran Shet"):
        self.search_input.click()
        self.search_input.fill(search_term)
        self.search_input.press("Enter")
        self.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(2)  
    
    def verify_no_blogs_found(self):
        self.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(2)
        no_blogs_locator = self.no_blogs_found.first
        no_blogs_locator.wait_for(state="visible", timeout=10000)
        no_blogs_text = no_blogs_locator.inner_text(timeout=5000)
        assert "No" in no_blogs_text and ("blog" in no_blogs_text.lower() or "result" in no_blogs_text.lower()), \
            f"Expected 'No blogs found' message but found: {no_blogs_text}"

    def verify_blogs_found_when_search_term_is_present(self, search_term="Getting Started with TypeScript"):
        self.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(2)
        assert self.blog_card_title.is_visible(timeout=10000), f"Expected blog title to be visible for search term '{search_term}' but no blog title is visible"

    def click_readmore_button(self):
        self.readmore_button = self.page.locator(LoginPageLocators.READMORE_BUTTON)
        self.readmore_button.click()

    def login_user(self):
        self.admin_button.click()
        self.username_field.click()
        self.username_field.fill(config["credentials"]["adminusername"])
        self.password_field.click()
        self.password_field.fill(config["credentials"]["password"])
        self.submit_button.click()
        self.logout_button.click()  
        time.sleep(10)
        
    def login_user_for_blog(self):
        self.admin_button.click()
        self.username_field.fill(config["credentials"]["adminusername"])
        self.submit_button.click()
        self.password_field.fill(config["credentials"]["password"])
        self.submit_button.click()
        self.blog_post_button.click()
        self.title_check.fill("Test Title")
        self.excerpt_check.click()
        self.excerpt_check.fill("hey Hi Are you there?")
        self.content_check.fill("This is a test content")
        self.category_check.click()
        self.category_option.click()
        self.tags_check.click()
        self.tags_check_option_1.click()
        self.page.locator("body").click(position={"x": 0, "y": 0})
        self.publish_now_button.click()
        self.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(2)  

    def login_user_for_blog_with_no_info(self):
        self.blog_post_button.click()
        self.title_check.fill("")
        self.excerpt_check.click()
        self.excerpt_check.fill("hey Hi Are you there?")
        self.content_check.fill("This is a test content")
        self.category_check.click()
        self.category_option.click()
        self.tags_check.click()
        self.tags_check_option_1.click()
        self.page.locator("body").click(position={"x": 0, "y": 0})    
        assert self.publish_now_button.is_disabled(), "Publish button should be disabled when title is empty"

    def verify_title_to_be_available_in_dashboard(self):
        self.page.wait_for_load_state("networkidle", timeout=15000)
        time.sleep(2) 
        title_locator = self.page.locator(LoginPageLocators.TEST_TITLE_CREATED).first
        title_locator.wait_for(state="visible", timeout=10000)
        title_text = title_locator.inner_text(timeout=5000)
        assert "Test Title" in title_text, f"Expected 'Test Title' but found: {title_text}"
    
    def click_delete_icon_for_blog(self, blog_title="Test Title"):
        self.delete_icon.click()
    
  
    def login_user_with_invalid_creds(self):
        self.username_field.click()
        self.admin_button.click()
        self.username_field.fill(config["credentials"]["invalid_username"])
        self.submit_button.click()
        self.password_field.fill(config["credentials"]["invalid_password"])
        self.submit_button.click()
        assert self.page.locator(LoginPageLocators.INVALID_CREDENTIALS_MESSAGE).is_visible()
        


        
