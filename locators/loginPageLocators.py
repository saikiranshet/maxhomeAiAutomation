class LoginPageLocators:
    ADMIN_BUTTON = "//*[@id='root']/header/div/div/a[2]"
    USERNAME_FIELD = '//*[@id=":r7:"]'
    PASSWORD_FIELD = '//*[@id=":r9:"]'
    SUBMIT_BUTTON = '//*[@id="auth-tabpanel-0"]/div/form/button'
    LOGOUT = "//*[@id='root']/header/div/div/button[1]"
    INVALID_CREDENTIALS_MESSAGE = "//*[contains(text(),'Invalid credentials')]"