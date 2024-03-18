class TextBoxPageLocators:

    # form fields
    FULL_NAME = ('xpath', '//*[@id="userName"]')
    EMAIL = ('xpath', '//*[@id="userEmail"]')
    CURRENT_ADDRESS = ('xpath', '//*[@id="currentAddress"]')
    PERMANENT_ADDRESS = ('xpath', '//*[@id="permanentAddress"]')
    SUBMIT = ('xpath', '//*[@id="submit"]')

    # created
    CREATED_FULL_NAME = ('xpath', '//*[@id="name"]')
    CREATED_EMAIL = ('xpath', '//*[@id="email"]')
    CREATED_CURRENT_ADDRESS = ('xpath', '(//p[@id="currentAddress"])[1]')
    CREATED_PERMANENT_ADDRESS = ('xpath', '(//p[@id="permanentAddress"])[1]')