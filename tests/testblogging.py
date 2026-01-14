import sys
import os
from POM.login import LoginPage

def test_ADM_LOGIN_01(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    login_page.login_user_for_blog()
    
    
