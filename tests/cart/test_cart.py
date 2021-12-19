class TestCart:
    def test_add_to_cart(self, app):
        """
        с00p
    Добавление товаров в корзину

    1) Перейти на страницу магазина
    2) Найти на странице товар
    3) В карточке товара нажать Buy
    4) Нажать на значок корзины
    5) Найти наименование добаленного товара
        """

        app.open_main_page()
        app.main.click_buy()
        prod_title = app.main.get_prod1_title()
        app.cart.open_cart()
        cart_title = app.cart.get_position_title(1)
        assert prod_title == cart_title

    def test_multi_add_to_cart(self, app):
        """
        c01p
    Добавление нескольких товаров в корзину

    1) Перейти на страницу магазина
    2) Найти на странице товар
    3) В карточке товара нажать Buy
    3.1) Нажать на кнопку Buy в карточке второгo  товара
    4) Открыть корзину
    5) Найти наименование первого и второго добаленного товара
        """

        app.open_main_page()
        app.main.click_buy()
        prod1_title = app.main.get_prod1_title()
        app.main.click_buy2()
        prod2_title = app.main.get_prod2_title()
        app.cart.open_cart()
        cart_title1 = app.cart.get_position_title(1)
        cart_title2 = app.cart.get_position_title(2)
        assert prod1_title == cart_title1 and prod2_title == cart_title2

    def test_remove_from_cart(self, app):
        """
        c02p

        Удаление товара из корзины

    1) Перейти на страницу магазина
    2) Найти на странице товар
    3) В карточке товара нажать Buy
    4) Нажать на значок корзины
    5) Найти наименование добаленного товара
    6)Нажать на кнопку удалить товар
        """

        app.open_main_page()
        app.main.click_buy()
        app.cart.open_cart()
        app.cart.remove_position(1)
        assert app.cart.get_empty_cart_status() is True

    def test_position_quant_up(self, app):

        """
        c03p

    Увеличение колличества товаров в корзине

    1) Перейти на страницу магазина
    2) Найти на странице товар
    3) В карточке товара нажать Buy
    4) Нажать на значок корзины
    5) Найти наименование добаленного товара
    6) Нажать на кнопку добавления колличества товара
        """

        app.open_main_page()
        app.main.click_buy()
        app.cart.open_cart()
        app.cart.position_quant_up(1)
        pos_quant = app.cart.get_position_quant(1)
        assert pos_quant == 2

    def test_position_quant_down(self, app):

        """
        c04p

    Уменьшение колличества товаров в корзине

    1) Перейти на страницу магазина
    2) Найти на странице товар
    3) В карточке товара нажать Buy
    3.1) В карточке товара еще раз нажать Buy
    4) Нажать на значок корзины
    5) Найти наименование добаленного товара
    6) Нажать на кнопку умененьшения колличества товара
        """

        app.open_main_page()
        app.main.click_buy()
        app.cart.open_cart()
        app.main.click_buy()
        app.cart.position_quant_down(1)
        pos_quant = app.cart.get_position_quant(1)
        assert pos_quant == 1

    def test_price_calc(self, app):
        """
        c05p

    Расчет стоимости товаров в корзине

    1) Перейти на страницу магазина
    2) Найти на странице товар
    3) В карточке товара нажать Buy
    4) В карточке ворого товара нажать Buy
    5) Нажать на значок корзины
    6) Найти наименование первого добавленного товара
    7) Найти наименование второго добавленного товара
    8) Найти строку Total price и стоимость покупки
        """

        app.open_main_page()
        main_page_price1 = app.main.get_position_price(1)
        app.main.click_buy()
        main_page_price2 = app.main.get_position_price(2)
        app.main.click_buy2()
        app.cart.open_cart()
        cart_page_price1 = app.cart.get_position_price(1)
        cart_page_price2 = app.cart.get_position_price(2)
        total_price = app.cart.get_total_price(2)
        assert total_price == cart_page_price1 + cart_page_price2
        assert main_page_price2 == cart_page_price2
        assert main_page_price1 == cart_page_price1

    def test_price_recalc_remove(self, app):
        """
        c06p

    Перерсчет стоимости товаров при удалении позиции из корзины

    1) Перейти на страницу магазина
    2) Найти на странице товар
    3) В карточке товара нажать Buy
    4) В карточке товара еще раз нажать Buy
    5) Нажать на значок корзины
    6) Найти наименование первого добавленного товара
    7) Найти наименование второго добавленного товара
    8) Найти строку Total price и стоимость покупки
    9) Удалить вторую позицию товара
     """

        app.open_main_page()
        app.main.click_buy()
        app.main.click_buy2()
        app.cart.open_cart()
        cart_page_price1 = app.cart.get_position_price(1)
        app.cart.remove_position(2)
        total_price = app.cart.get_total_price(1)
        assert cart_page_price1 == total_price

    def test_price_recalc_pos_up(self, app):
        """
        c07p

    Перерасчет стоимости товаров увеличении колличества позиции из корзины

    1) Перейти на страницу магазина
    2) Найти на странице товар
    3) В карточке товара нажать Buy
    4) Нажать на значок корзины
    5) Нажать кнопку + у нименования товара
     """

        app.open_main_page()
        app.main.click_buy()
        app.cart.open_cart()
        cart_page_price = app.cart.get_position_price(1)
        app.cart.position_quant_up(1)
        pos_quant = app.cart.get_position_quant(1)
        total_price = app.cart.get_total_price(1)
        assert pos_quant * cart_page_price == total_price

    def test_price_recalc_pos_down(self, app):
        """
        c08p

    Перерасчет стоимости товаров уменьшении колличества позиции из корзины

    1) Перейти на страницу магазина
    2) Найти на странице товар
    3) В карточке товара дважды нажать Buy
    4) Нажать на значок корзины
    5) Нажать кнопку - у нименования товара
     """

        app.open_main_page()
        app.main.click_buy()
        app.main.click_buy()
        app.cart.open_cart()
        app.cart.position_quant_down(1)
        cart_page_price = app.cart.get_position_price(1)
        pos_quant = app.cart.get_position_quant(1)
        total_price = app.cart.get_total_price(1)
        assert pos_quant * cart_page_price == total_price

    def test_buying(self, app):
        """
               c09p

           Покупка товара

    1) Перейти на страницу магазина
    2) Найти на странице товар
    3) В карточке товара нажать Buy
    4) Нажать на значок корзины
    5) Найти наименование добаленного товара
    6) Нажать на кнопку Buy
            """

        app.open_main_page()
        app.main.click_buy()
        app.cart.open_cart()
        app.cart.buy()
        assert app.cart.get_empty_cart_status() is True


