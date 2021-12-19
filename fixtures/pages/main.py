import logging

from fixtures.locators.main import MainLocators
from fixtures.models.main import Product
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class MainPage(BasePage):
    def get_prod1_title(self) -> str:
        title = self.get_text(MainLocators.ITEM1)
        logger.info(f"Название товара {title}")
        return title

    def get_prod2_title(self) -> str:
        title = self.get_text(MainLocators.ITEM2)
        logger.info(f"Название второго товара {title}")
        return title

    def fill_bar_filler(self, prod: str):
        self.fill_element(prod, MainLocators.SEARCH_BAR)
        logger.info(f"Ввели в строку поиса значение {prod}")

    def click_search_button(self):
        self.click_element(MainLocators.SEARCH_BUTTON)
        logger.info(f"Нажали кнопку Search")

    def click_prpr_ata(self):
        self.click_element(MainLocators.PRPR_ATA)
        logger.info(f"Вызвали подготовку данных")

    def get_positive_search(self):
        return self.get_text(MainLocators.POSITIVE_SEARCH_RESULT)

    def get_negative_search_result(self) -> str:
        result = self.get_text(MainLocators.NEGATIVE_SEARCH_RESULT)
        logger.info(f"Найдена строка {result}")
        return result

    def get_invalid_prod_title(self) -> str:
        title = Product.INVALID_SEARCH
        return title

    def error_ref(self) -> str:
        ref = Product.ERROR_REF
        return ref

    def click_buy(self):
        self.click_element(MainLocators.BUY_BUTTON)
        logger.info(f"Нажали кнопку Buy")

    def click_buy2(self):
        self.click_element(MainLocators.BUY_BUTTON2)
        logger.info(f"Нажали кнопку Buy")

    def get_message_text(self) -> str:
        message = self.get_text(MainLocators.MESSAGE)
        logger.info(f"Получено сообщение {message}")
        return message

    def buy_first_message_composer(self) -> str:
        title: str = self.get_prod1_title()
        message: str = title + ' add to cart'
        return message

    def buy_second_message_composer(self) -> str:
        title: str = self.get_prod2_title()
        message: str = title + ' add to cart'
        return message

    def get_count_number(self) -> int:
        counter = self.get_text(MainLocators.COUNTER_CART)
        logger.info(f"Значение счетчика {counter}")
        count: int = int(counter)
        return count

    def get_position_price(self, pos_number: int) -> int:
        if pos_number == 1:
            pos_price_str: str = self.get_text(MainLocators.ITEM1_PRICE)
        else:
            pos_price_str: str = self.get_text(MainLocators.ITEM2_PRICE)

        price = int(self.string_word_extractor(1, pos_price_str))
        logger.info(f"Итоговая цена позиции №{pos_number} равна {price}")
        return price

