import allure
from selene import browser, have, be


class MainPage:
    @allure.step('Открыть главную страницу')
    def open(self):
        browser.open('/')

    @allure.step('Переход на страницу авторизации')
    def go_to_authorization(self):
        browser.element('[href="/login/"][itemscope="itemscope"]').click()

    @allure.step('Открыть форму регистрации')
    def registration_form(self):
        browser.element('[href="/register/"][itemscope="itemscope"]').click()

    @allure.step('Выбор бесплатного тарифа')
    def free_plan(self):
        browser.element('.menu-item [href="/subscription/"]').click()
        browser.element('[data-tariff-head="1"] .ms-button-outline-primary').click()

    @allure.step('Поиск маркетплейса')
    def search_marketplace(self):
        browser.element('.menu-item  [href="/poleznoe/marketplejsy/"]').click()
        browser.element('[type="text"][placeholder="Найти статью"]').should(be.blank).type('озон').press_enter()

    @allure.step('Переход на youtube канал')
    def go_to_youtube_channel(self):
        browser.element('[href="https://www.youtube.com/moysklad/"]').click()