from selenium.webdriver.common.by import By


class MainLocators:
    SEARCH_BAR = (By.ID, "email_inline")
    SEARCH_BUTTON = (By.XPATH, "//div[@id='root']/div/main/div/button")
    ITEM1 = (By.XPATH, '//*[@id="root"]/div/main/div[3]/div[1]/div[2]/span')
    ITEM2 = (By.XPATH, '//*[@id="root"]/div/main/div[3]/div[2]/div[2]/span')
    BUY_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div[3]/div[1]/div[3]/button')
    BUY_BUTTON2 = (By.XPATH, '//*[@id="root"]/div/main/div[3]/div[2]/div[3]/button')
    PRPR_ATA = (By.XPATH, "//button[contains(.,'Prepere data')]")
    POSITIVE_SEARCH_RESULT = (By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/span')
    NEGATIVE_SEARCH_RESULT = (By.XPATH, '//*[@id="root"]/div/main/div[3]/h3')
    MESSAGE = (By.XPATH, '//*[@id="toast-container"]/div')
    COUNTER_CART = (By.XPATH,'//*[@id="root"]/div/main/div[2]/span')