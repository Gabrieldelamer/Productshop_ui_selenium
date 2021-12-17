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
    DELETE_FIRST_ITEM = (By.XPATH, '//*[@id="root"]/div/main/ui/li[2]/span/i')
    DELETE_SECOND_ITEM = (By.XPATH, '//*[@id="root"]/div/main/ui/li[3]/span/i')
    ADD_FIRST_POSITION_QUANT = (By.XPATH, '//*[@id="root"]/div/main/ui/li[2]/i[2]')
    REMOVE_FIRST_POSISTION_QUANT = (By.XPATH, '//*[@id="root"]/div/main/ui/li[2]/i[1]')
    BY_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/ui/li[5]/button')
    CLOSE_CART = (By.XPATH, '//*[@id="root"]/div/main/ui/i')


