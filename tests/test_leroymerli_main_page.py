import allure
from allure_commons.types import Severity
from leroymerlin_tests.pages.main_page import MainPage

main_page = MainPage()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Zverev Daniil')
@allure.feature('Main page')
@allure.story('Прооверка перехода на главную страницу')
@allure.link('https://leroymerlin.ru/')
def test_assert_elements_texts():
    main_page.open()

    main_page.go_to_authorization()