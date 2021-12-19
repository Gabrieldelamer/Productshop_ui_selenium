import webdriver_manager.utils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, app):
        self.app = app

    def custom_find_element(self, locator, wait_time=60):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def click_element(self, locator, wait_time=60):
        """
        click_element = click
        """
        element = self.custom_find_element(locator, wait_time)
        element.click()

    def d_click_element(self, locator, wait_time=60):
        """
        click_element = click
        """
        element = self.custom_find_element(locator, wait_time)
        element.double_click()

    def fill_element(self, data, locator, wait_time=60):
        """
        Fill element (fill_element == send_keys)
        :param data: string to fill
        """
        element = self.custom_find_element(locator, wait_time)
        if data:
            element.send_keys(data)

    def get_text(self, locator, wait_time=60) -> str:

        element = self.custom_find_element(locator, wait_time)
        return element.text

    def get_inner_text(self, locator, wait_time=60) -> str:
        """
        Get element text
        """
        element = self.custom_find_element(locator, wait_time)
        return element.get_attribute('innerText')

    def string_word_extractor(self, word_number: int, string: str) -> str:
        position_list: list = string.split(" ")
        it_title = iter(position_list)
        index_list: list = []
        for i in range(1, len(position_list)):
            index_list.append(i)

        title_words = dict(zip(index_list, it_title))
        title = title_words[word_number]
        return title

    def int_str_extrator(self, string: str):
        num = ""
        for c in string:
            if c.isdigit():
                num = int(num + c)
        return num
