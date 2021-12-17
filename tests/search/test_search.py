class TestSearch:
    def test_prp_ata(self,app):
        """
        Предварительные условия

        Подготовить данные для поиска

        """


        app.open_main_page()
        app.main.click_search_button()
        app.main.click_prpr_ata()
        app.refresh_page()
        app.open_main_page()
        prod = app.main.get_prod1_title()
        assert prod != None

    def test_valid_item(self, app):
        """
        s01p

        1) переходим на страницу магазина
        2) вводим наименования имеющегося товара
        3) нажимаем кнопку Search
        4) находим на странице результатов поиска искомый товар

        """
        app.open_main_page()
        prod = app.main.get_prod1_title()
        app.main.fill_bar_filler(prod)
        app.main.click_search_button()
        search_result_item = app.main.get_prod1_title()
        assert search_result_item == prod

    def test_invalid_item(self, app):
        """
                s02n
                Поиск несуществующего наименования товара

                1) переходим на страницу магазина
                2) вводим наименования несуществующего товара
                3) нажимаем кнопку Search
                4) находим на странице результатов текст
                   с сообщением Nothing here, see github

                """

        app.open_main_page()
        title = app.main.get_invalid_prod_title()
        app.main.fill_bar_filler(title)
        app.main.click_search_button()
        error_message = app.main.get_negative_search_result()
        error_ref = app.main.error_ref()
        assert error_message == error_ref

    def test_empty_item(self, app):
        """
                s03n
                Поиск несуществующего наименования товара

                1) переходим на страницу магазина
                2) нажимаем кнопку Search
                3) находим на странице результатов текст
                   с сообщением Nothing here, see github

                """

        app.open_main_page()
        app.main.click_search_button()
        error_message = app.main.get_negative_search_result()
        error_ref = app.main.error_ref()
        assert error_message == error_ref
