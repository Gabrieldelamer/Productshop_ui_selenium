from fixtures.pages.base_page import BasePage
from fixtures.locators.cart import CartLocators

class CartPage(BasePage):

    def open_cart(self):
        self.click_element(CartLocators.CART_BUTTON)


    def get_first_position_quant(self):
        pos_arr = self.get_text(CartLocators.FIRST_POSITION_QUANT)
        print(pos_arr)

    def get_second_position_quant(self):
        pass

#    def



