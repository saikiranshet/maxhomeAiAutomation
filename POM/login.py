
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
        
    def login_user(self):
        self.admin_button.click()
        self.username_field.fill(config["credentials"]["adminusername"])
        self.submit_button.click()
        self.password_field.fill(config["credentials"]["password"])
        self.submit_button.click()
        self.logout_button.first.click()  # Wait for logout button to appear
        time.sleep(10)
        
    def login_user_for_blog(self):
        self.admin_button.click()
        self.username_field.fill(config["credentials"]["adminusername"])
        self.submit_button.click()
        self.password_field.fill(config["credentials"]["password"])
        self.submit_button.click()
        time.sleep(10)

    def login_user_with_invalid_creds(self):
        self.admin_button.click()
        self.username_field.fill(config["credentials"]["invalid_username"])
        self.submit_button.click()
        self.password_field.fill(config["credentials"]["invalid_password"])
        self.submit_button.click()
        assert self.page.locator(LoginPageLocators.INVALID_CREDENTIALS_MESSAGE).is_visible()
        


        
