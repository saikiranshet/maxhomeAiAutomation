
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


    def login_user(self):
        self.admin_button.click()
        self.username_field.click()
        self.username_field.fill(config["credentials"]["adminusername"])
        self.password_field.click()
        self.password_field.fill(config["credentials"]["password"])
        self.submit_button.click()
        self.logout_button.click()  # Wait for logout button to appear
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

    def verify_tille_to_be_available(self):
        # self.
        

    def login_user_with_invalid_creds(self):
        self.username_field.click()
        self.admin_button.click()
        self.username_field.fill(config["credentials"]["invalid_username"])
        self.submit_button.click()
        self.password_field.fill(config["credentials"]["invalid_password"])
        self.submit_button.click()
        assert self.page.locator(LoginPageLocators.INVALID_CREDENTIALS_MESSAGE).is_visible()
        


        
