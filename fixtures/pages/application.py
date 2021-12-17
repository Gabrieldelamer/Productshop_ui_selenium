from fixtures.pages.main import MainPage
from fixtures.pages.cart import CartPage
import time


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.main = MainPage(self)
        self.cart = CartPage(self)

    def quit(self):
        self.driver.quit()

    def open_main_page(self):
        self.driver.get(self.url)
        time.sleep(2)

    def refresh_page(self):
        self.driver.refresh()

    # def prepapre_data(self):
