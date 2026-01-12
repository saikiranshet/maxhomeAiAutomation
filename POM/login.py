
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
        self.submit_button1 = page.locator(LoginPageLocators.SUBMIT_BUTTON)


    def login_user(self):
        self.admin_button.click()
        time.sleep(2)
        self.username_field.fill(config["credentials"]["adminusername"])
        time.sleep(1)
        self.submit_button1.click()
        time.sleep(1)
        self.password_field.fill(config["credentials"]["password"])
        time.sleep(1)
        self.submit_button1.click()
        time.sleep(20)


        
