class LoginPageLocators:
    ADMIN_BUTTON = "//*[@id='root']/header/div/div/a[2]"
    USERNAME_FIELD = '//*[@id=":r7:"]'
    PASSWORD_FIELD = '//*[@id=":r9:"]'
    SUBMIT_BUTTON = '//*[@id="auth-tabpanel-0"]/div/form/button'
    LOGOUT = "//*[contains(text(),'Logout')]"
    INVALID_CREDENTIALS_MESSAGE = "//*[contains(text(),'Invalid credentials')]"
    BLOG_POST_BUTTON = "//*[contains(text(),'New Blog Post')]"
    TITLE_CHECK = "//label[contains(text(),'Title')]/following::input[1]"
    EXCERPT_CHECK = "//label[contains(text(),'Excerpt')]/following::textarea[1]"
    CONTENT_CHECK = "//*[@id='root']/div/div/form/div[4]/div/div[2]/div[1]"
    CONTENT_CLICK = '//*[contains(text(),"Content")]'
    # CONTENT_CHECK = "//*[@id='root']/div/div/form/div[4]/div/div[2]/div[1]"
    CATEGORY_CHECK = "//label[contains(text(),'Category')]/following::div[1]"
    CATEGORY_OPTION = "//*[contains(text(),'Technology')]"
    TAGS_CHECK = "//label[contains(text(),'Tags')]/following::div[1]"
    TAGS_CHECK_OPTION_1 = "//*[contains(text(),'JavaScript')]"
    TAGS_CHECK_OPTION_2 = "//*[contains(text(),'TypeScript')]"
    TAGS_CHECK_OPTION_3 = "//*[contains(text(),'React')]"
    TAGS_CHECK_OPTION_4 = "//*[contains(text(),'Node.js')]"
    PUBLISH_NOW_BUTTON = "//*[contains(text(),'Publish Now')]"
    SAVE_BUTTON = "//*[contains(text(),'Save')]"
    CANCEL_BUTTON = "//*[contains(text(),'Cancel')]"