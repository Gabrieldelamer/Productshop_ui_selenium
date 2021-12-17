class TestBuy:
    def test_add_to_cart(self, app):
        """
        a01p
        Добавление товара в корзину

        1) Перейти на страницу магазина
        2) Найти первый товар в списке
        3) Нажать кнопку Buy в карточке товара
        4) В верхнем правом углу появиться
           сообщение о добавлении товара.

        """
        app.open_main_page()
        app.main.click_buy()
        message = app.main.get_message_text()
        ref_message = app.main.buy_first_message_composer()
        assert message == ref_message

    def test_add_to_cart_two_items(self, app):
        """
        a02p
        Добавление нескольких товаров в корзину

        1) Перейти на страницу магазина
        2) Найти первый товар в списке
        3) Нажать кнопку Buy в карточке товара
        4) В верхнем правом углу появиться
           сообщение о добавлении товара.
        5) Найти второй товар
        6) Нажать кнопку Buy в карточке второго товара
        7) В верхнем правом углу появиться
           сообщение о добавлении товара.

        """
        app.open_main_page()
        app.main.click_buy()
        message1 = app.main.get_message_text()
        ref_message1 = app.main.buy_first_message_composer()
        app.main.click_buy2()
        message2 = app.main.get_message_text()
        ref_message2 = app.main.buy_second_message_composer()
        assert message2 == ref_message2 and message1 == ref_message1

    def test_check_item_counter_increasing(self, app):
        """
               a03p
               Добавление нескольких товаров в корзину

               1) Перейти на страницу магазина
               2) Найти первый товар в списке
               3) Нажать кнопку Buy в карточке товара
               4) Значение счетчика равно 1
               5) Найти второй товар
               6) Нажать кнопку Buy в карточке второго товара
               7) Значение счетчика равно 2

               """
        app.open_main_page()
        app.main.click_buy()
        counter1 = app.main.get_count_number()
        app.main.click_buy2()
        counter2 = app.main.get_count_number()
        assert counter1 == 1 and counter2 == 2

    def test_check_item_counter_duplicate(self, app):
        """
               a04n
               Добавление нескольких товаров в корзину

               1) Перейти на страницу магазина
               2) Найти первый товар в списке
               3) Нажать кнопку Buy в карточке товара
               4) Значение счетчика равно 1
               5) Нажать кнопку Buy в карточке товара
               6) Значение счетчика равно 1

               """
        app.open_main_page()
        app.main.click_buy()
        counter1 = app.main.get_count_number()
        app.main.click_buy()
        counter2 = app.main.get_count_number()
        assert counter1 == 1 and counter2 == 1
