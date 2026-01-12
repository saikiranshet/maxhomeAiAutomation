import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from POM.login import LoginPage

def test_loginAdmin(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    login_page.login_user()
