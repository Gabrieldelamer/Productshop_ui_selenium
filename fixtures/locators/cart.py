from selenium.webdriver.common.by import By


class CartLocators:
    CART_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div[2]/i')
    FIRST_POSITION_QUANT = (By.XPATH, '//*[@id="root"]/div/main/ui/li[2]/i[1]')
    SECOND_POSITION_QUANT = (By.XPATH, '//*[@id="root"]/div/main/ui/li[3]/i[1]')
    FIRST_POSITION_TITLE = (By.XPATH, '//*[@id="root"]/div/main/ui/li[2]')
    SECOND_POSITION_TITLE = (By.XPATH, '//*[@id="root"]/div/main/ui/li[3]')
    TOTAL_PRICE_FIRST_POSITION = (By.XPATH, '//*[@id="root"]/div/main/ui/li[2]/i[2]')
    TOTAL_PRICE_SECOND_POSITION = (By.XPATH, '//*[@id="root"]/div/main/ui/li[3]/i[2]')
    TOTAL_PRICE = (By.XPATH, '//*[@id="root"]/div/main/ui/li[4]')
    TOTAL_PRICE_REMOVED = (By.XPATH, '//*[@id="root"]/div/main/ui/li[3]')
    DELETE_FIRST_ITEM = (By.XPATH, '//*[@id="root"]/div/main/ui/li[2]/span/i')
    DELETE_SECOND_ITEM = (By.XPATH, '//*[@id="root"]/div/main/ui/li[3]/span/i')
    ADD_FIRST_POSITION_QUANT = (By.CSS_SELECTOR, '.collection-item:nth-child(2) > .material-icons:nth-child(2)')
    ADD_SECOND_POSITION_QUANT = (By.XPATH, '//*[@id="root"]/div/main/ui/li[3]/i[2]')
    DOWN_FIRST_POSISTION_QUANT = (By.CSS_SELECTOR, ".basket-quantity:nth-child(1)")
    DOWN_SECOND_POSISTION_QUANT = (By.XPATH, '//*[@id="root"]/div/main/ui/li[3]/i[1]')
    BUY_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/ui/li[4]/button')
    CART_IS_EMPTY = (By.XPATH, '//*[@id="root"]/div/main/ui/li[2]')
    PAY_DONE_MESSAGE = (By.XPATH, '//*[@id="toast-container"]/div')
    CLOSE_CART = (By.XPATH, '//*[@id="root"]/div/main/ui/i')


