import sys
import os
from POM.login import LoginPage


def test_ADM_LOGIN_01(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.login_user()
    finally:
        login_page.logout_user()


def test_ADM_LOGIN_02(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    login_page.reload_page()
    login_page.home_screen()
    try:
        login_page.login_user_with_invalid_creds()
    finally:
        login_page.home_screen()
    

