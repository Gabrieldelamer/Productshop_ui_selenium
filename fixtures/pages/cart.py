from fixtures.pages.base_page import BasePage
from fixtures.locators.cart import CartLocators
from fixtures.models.cart import CartConst
import logging

logger = logging.getLogger("moodle")


class CartPage(BasePage):

    def open_cart(self):
        self.click_element(CartLocators.CART_BUTTON)

    def get_position_quant(self, pos_number: int) -> int:
        if pos_number == 1:
            position_string = (self.get_text(CartLocators.FIRST_POSITION_TITLE))
        else:
            position_string = (self.get_text(CartLocators.SECOND_POSITION_TITLE))
        multiplayer_str = str(self.string_word_extractor(3, position_string))
        mutiplayer = self.int_str_extrator(multiplayer_str)
        return mutiplayer

    def get_position_title(self, pos_number: int) -> str:
        if pos_number == 1:
            title_string: str = self.get_text(CartLocators.FIRST_POSITION_TITLE)
        else:
            title_string: str = self.get_text(CartLocators.SECOND_POSITION_TITLE)

        title: str = self.string_word_extractor(1, title_string)
        logger.info(f"Наименование товара №{pos_number} {title}")
        return title

    def get_total_price(self, pos_q) -> int:
        if pos_q == 2:
           totalI_price_string = self.get_text(CartLocators.TOTAL_PRICE)
        else:
           totalI_price_string = self.get_text(CartLocators.TOTAL_PRICE_REMOVED)
        total_price = int(self.string_word_extractor(3, totalI_price_string))
        logger.info(f"Итоговая стоимость заказа равна {total_price}")
        return total_price

    def get_position_price(self, pos_number: int) -> int:
        if pos_number == 1:
           position_price: str = (self.get_text(CartLocators.FIRST_POSITION_TITLE))
        else:
            position_price: str = (self.get_text(CartLocators.SECOND_POSITION_TITLE))
        price_str = str(self.string_word_extractor(6, position_price))
        price_int: int = int(price_str)
        logger.info(f"Итоговая цена позиции №{position_price} равна {price_int}")
        return price_int

    def buy(self):
        self.click_element(CartLocators.BUY_BUTTON)

    def open_cart(self):
        self.click_element(CartLocators.CART_BUTTON)
        logger.info(f"Открываем корзину")

    def remove_position(self, pos_number: int):
        if pos_number == 1:
            self.click_element(CartLocators.DELETE_FIRST_ITEM)
        else:
            self.click_element(CartLocators.DELETE_SECOND_ITEM)
        logger.info(f"Удалили позицию №{pos_number}")

    def position_quant_up(self, pos_number: int):
        if pos_number == 1:
            self.click_element(CartLocators.ADD_FIRST_POSITION_QUANT)
            logger.info(f"Добавлена одна единица {pos_number}-го товара")
        else:
            self.click_element(CartLocators.ADD_SECOND_POSITION_QUANT)
            logger.info(f"Добавлена одна единица {pos_number}-го товара")

    def position_quant_down(self, pos_number: int):
        if pos_number == 1:
            self.click_element(CartLocators.DOWN_FIRST_POSISTION_QUANT)
            logger.info(f"Удалена одна единица {pos_number}-го товара")
        else:
            self.click_element(CartLocators.DOWN_SECOND_POSISTION_QUANT)
            logger.info(f"Удалена одна единица {pos_number}-го товара")

    def close_cart(self):
        self.click_element(CartLocators.CLOSE_CART)

    def get_empty_cart_status(self):
        message_on_page = self.get_text(CartLocators.CART_IS_EMPTY)
        if message_on_page == CartConst.EMPTY_CART_MESS:
            logger.info(f"Корзина пуста")
            return True
        else:
            logger.info(f"Корзина не пуста")
            return False

    def get_success_message(self) -> str:
        return self.get_text(CartLocators.PAY_DONE_MESSAGE)



