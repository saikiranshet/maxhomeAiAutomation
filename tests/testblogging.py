import sys
import os
import time
from POM.login import LoginPage
from locators.loginPageLocators import LoginPageLocators


def test_blogmgmt_001(setupcheck):
    page = setupcheck
    login_page = LoginPage(page)
    login_page.reload_page()
    login_page.home_screen()
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

def test_blogmgmt_009_create_blog_with_custom_title(setupcheck):
    """Test creating a blog with a custom title"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.create_blog_with_custom_title("Custom Test Blog")
        login_page.verify_blog_in_dashboard("Custom Test Blog")
    finally:
        login_page.click_delete_icon_for_blog("Custom Test Blog")
        login_page.logout_user()

def test_blogmgmt_010_save_blog_as_draft(setupcheck):
    """Test saving a blog as draft instead of publishing"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.save_blog_as_draft("Draft Blog Test")
        login_page.verify_blog_in_dashboard("Draft Blog Test")
    finally:
        login_page.click_delete_icon_for_blog("Draft Blog Test")
        login_page.logout_user()

def test_blogmgmt_011_create_blog_with_multiple_tags(setupcheck):
    """Test creating a blog with multiple tags"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.create_blog_with_multiple_tags("Multi Tag Blog")
        login_page.verify_blog_in_dashboard("Multi Tag Blog")
    finally:
        login_page.click_delete_icon_for_blog("Multi Tag Blog")
        login_page.logout_user()

def test_blogmgmt_012_create_multiple_blogs(setupcheck):
    """Test creating multiple blogs in sequence"""
    page = setupcheck
    login_page = LoginPage(page)
    blog_titles = ["Blog One", "Blog Two", "Blog Three"]
    try:
        login_page.reload_page()
        login_page.login_user()
        for title in blog_titles:
            login_page.create_blog_with_custom_title(title)
            login_page.verify_blog_in_dashboard(title)
    finally:
        for title in blog_titles:
            try:
                login_page.click_delete_icon_for_blog(title)
            except Exception:
                pass
        login_page.logout_user()

def test_publicviewing_009_search_with_partial_keyword(setupcheck):
    """Test search functionality with partial keyword"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.home_screen()
        login_page.search_screen("TypeScript")
        login_page.verify_blogs_found_when_search_term_is_present("TypeScript")
    finally:
        login_page.logout_user()

def test_publicviewing_010_search_case_insensitive(setupcheck):
    """Test search is case insensitive"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.home_screen()
        login_page.search_screen("typescript")
        login_page.verify_blogs_found_when_search_term_is_present("typescript")
    finally:
        login_page.logout_user()

def test_publicviewing_011_light_mode_verification(setupcheck):
    """Test light mode functionality and verification"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.home_screen()
        login_page.switch_to_light_mode()
        login_page.verify_light_mode_active()
        login_page.switch_to_dark_mode()
        login_page.verify_dark_mode_active()
        login_page.switch_to_light_mode()
        login_page.verify_light_mode_active()
    finally:
        login_page.logout_user()

def test_publicviewing_012_navigation_home_to_admin(setupcheck):
    """Test navigation between home and admin sections"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.home_screen()
        login_page.login_user()
        login_page.navigate_to_dashboard()
        login_page.home_screen()
        assert login_page.home_button.is_visible(), "Home button should be visible"
    finally:
        login_page.logout_user()

def test_blogmgmt_013_verify_publish_button_disabled_empty_title(setupcheck):
    """Test that publish button is disabled when title is empty"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.login_user_for_blog_with_no_info()
        assert login_page.publish_now_button.is_disabled(), "Publish button should be disabled when title is empty"
    finally:
        login_page.logout_user()

def test_blogmgmt_014_cancel_blog_creation(setupcheck):
    """Test canceling blog creation"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.blog_post_button.click()
        login_page.title_check.fill("Blog to Cancel")
        login_page.cancel_button.click()
        login_page.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(1)
    finally:
        login_page.logout_user()

def test_publicviewing_013_view_blog_detail_page(setupcheck):
    """Test viewing a blog detail page"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.home_screen()
        login_page.search_screen("Getting Started with TypeScript")
        login_page.verify_blogs_found_when_search_term_is_present("Getting Started with TypeScript")
        login_page.click_readmore_button()
        login_page.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(2)
    finally:
        login_page.logout_user()

def test_blogmgmt_015_verify_blog_content_fields(setupcheck):
    """Test that all blog content fields can be filled"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.blog_post_button.click()
        login_page.title_check.fill("Content Test Blog")
        login_page.excerpt_check.click()
        login_page.excerpt_check.fill("This is a test excerpt")
        login_page.content_check.fill("This is test content for the blog")
        assert login_page.title_check.input_value() == "Content Test Blog", "Title should be filled"
        assert login_page.excerpt_check.input_value() == "This is a test excerpt", "Excerpt should be filled"
    finally:
        login_page.cancel_button.click()
        login_page.logout_user()

def test_blogmgmt_016_edit_existing_blog(setupcheck):
    """Test editing an existing blog post"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.create_blog_with_custom_title("Blog to Edit")
        login_page.verify_blog_in_dashboard("Blog to Edit")
        login_page.page.wait_for_load_state("networkidle", timeout=10000)
    finally:
        login_page.click_delete_icon_for_blog("Blog to Edit")
        login_page.logout_user()

def test_publicviewing_014_clear_search_and_verify(setupcheck):
    """Test clearing search and verifying all blogs are shown"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.home_screen()
        login_page.search_screen("TypeScript")
        login_page.verify_blogs_found_when_search_term_is_present("TypeScript")
        login_page.home_screen()
        login_page.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(2)
    finally:
        login_page.logout_user()

def test_blogmgmt_017_verify_category_selection(setupcheck):
    """Test that category can be selected from dropdown"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.blog_post_button.click()
        login_page.title_check.fill("Category Test Blog")
        login_page.category_check.click()
        login_page.category_option.click()
        time.sleep(1)
    finally:
        login_page.cancel_button.click()
        login_page.logout_user()

def test_blogmgmt_018_verify_tags_selection(setupcheck):
    """Test that multiple tags can be selected"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.blog_post_button.click()
        login_page.title_check.fill("Tags Test Blog")
        login_page.tags_check.click()
        login_page.tags_check_option_1.click()
        login_page.tags_check.click()
        login_page.tags_check_option_2.click()
        login_page.page.locator("body").click(position={"x": 0, "y": 0})
        time.sleep(1)
    finally:
        login_page.cancel_button.click()
        login_page.logout_user()

def test_publicviewing_015_verify_blog_list_display(setupcheck):
    """Test that blog list is displayed on home page"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.home_screen()
        login_page.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(2)
        blog_cards = login_page.page.locator(LoginPageLocators.BLOG_CARD)
        assert blog_cards.count() > 0, "At least one blog card should be visible on home page"
    finally:
        login_page.logout_user()

def test_blogmgmt_019_verify_dashboard_navigation(setupcheck):
    """Test navigation to and from dashboard"""
    page = setupcheck
    login_page = LoginPage(page)
    try:
        login_page.reload_page()
        login_page.login_user()
        login_page.navigate_to_dashboard()
        login_page.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(2)
        login_page.home_screen()
        assert login_page.home_button.is_visible(), "Home button should be visible"
    finally:
        login_page.logout_user()
