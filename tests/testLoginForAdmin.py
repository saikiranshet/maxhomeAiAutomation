import sys
import os
from POM.login import LoginPage


def test_ADM_LOGIN_01(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    login_page.login_user()


def test_ADM_LOGIN_02(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    page.reload()
    login_page.login_user_with_invalid_creds()

