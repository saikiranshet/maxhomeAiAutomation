import sys
import os
from POM.login import LoginPage


def test_blogmgmt_001(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.login_user()
        login_page.login_user_for_blog()
        login_page.verify_title_to_be_available_in_dashboard()
    finally:
        login_page.click_delete_icon_for_blog("Test Title")
        login_page.logout_user()
    
def test_blogmgmt_002(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.login_user_for_blog_with_no_info()
    finally:
        login_page.logout_user()

def test_blogmgmt_003_delete_blog(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.login_user_for_blog()
        login_page.verify_title_to_be_available_in_dashboard()
        login_page.click_delete_icon_for_blog("Test Title")
    finally:
        login_page.logout_user()

def test_blogmgmt_004_delete_blog_cancel(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.login_user_for_blog()
        login_page.verify_title_to_be_available_in_dashboard()
        login_page.delete_1st_icon.click()
        login_page.verify_title_to_be_available_in_dashboard()
        login_page.cancel_delete_button.click()
    finally:
        login_page.logout_user()

def test_publicviewing_005_no_blogs_found(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.home_screen()
        login_page.search_screen("Saikiran Shet")
        login_page.verify_no_blogs_found()
    finally:
        login_page.logout_user()

def test_publicviewing_006_blogs_found_exact_title(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.home_screen()
        login_page.search_screen("Getting Started with TypeScript")
        login_page.verify_blogs_found_when_search_term_is_present("Getting Started with TypeScript")
    finally:
        login_page.logout_user()

def test_publicviewing_007_switch_to_dark_mode(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.home_screen()
        login_page.switch_to_dark_mode()
        login_page.verify_dark_mode_active()
    finally:
        login_page.reload_page()
        login_page.switch_to_light_mode()

def test_publicviewing_008_readmore(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.home_screen()
        login_page.search_screen("Getting Started with TypeScript")
        login_page.verify_blogs_found_when_search_term_is_present("Getting Started with TypeScript")
        login_page.click_readmore_button()
    finally:
        login_page.logout_user()

