import allure
from selene import browser, have, be


class MainPage:
    @allure.step('Открыть главную страницу')
    def open(self):
        browser.open('')

    @allure.step('Переход на страницу авторизации')
    def go_to_authorization(self):
        browser.element('[data-qa="auth-button"]').click()
        browser.element('[data-qa-header-user-auth="login"]').click()
        browser.element('._3ZkVWJ-JEE_customer').should(have.exact_texts('Авторизация'))

    @allure.step('Переход в корзину')
    def go_to_basket(self):
        browser.element('[data-qa="header-basket-button"]').click()
        browser.element('._2U4nfHXIK4 ').should(have.exact_texts('В корзине пусто'))

    @allure.step('Переход в корзину')
    def check_search(self):
        browser.element('[data-qa-search-input="true"]').should(be.blank).type('обои')
        browser.element('[data-qa-search-button]').click()
        browser.element('[data-qa-title]').should(have.exact_texts('Товары по запросу «обои»'))