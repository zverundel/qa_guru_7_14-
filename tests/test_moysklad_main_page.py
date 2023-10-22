import allure
from allure_commons.types import Severity
from moysklad_tests.pages.main_page import MainPage

main_page = MainPage()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Zverev Daniil')
@allure.feature('Main page')
@allure.story('Прооверка авторизации')
@allure.link('https://www.moysklad.ru/')
def test_open_authorization():
    main_page.open()

    main_page.go_to_authorization()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Zverev Daniil')
@allure.feature('Main page')
@allure.story('Прооверка регистрации')
@allure.link('https://www.moysklad.ru/')
def test_open_registration_form():
    main_page.open()

    main_page.registration_form()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Zverev Daniil')
@allure.feature('Main page')
@allure.story('Прооверка тарифа')
@allure.link('https://www.moysklad.ru/')
def test_check_free_plan():
    main_page.open()

    main_page.free_plan()

@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Zverev Daniil')
@allure.feature('Main page')
@allure.story('Прооверка поиска маркетплейса')
@allure.link('https://www.moysklad.ru/')
def test_search_marketplace():
    main_page.open()

    main_page.search_marketplace()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Zverev Daniil')
@allure.feature('Main page')
@allure.story('Прооверка перехода на youtube канал')
@allure.link('https://www.moysklad.ru/')
def test_open_youtube_channel():
    main_page.open()

    main_page.go_to_youtube_channel()