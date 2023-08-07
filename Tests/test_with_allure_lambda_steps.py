from allure_commons.types import Severity
from selene import browser, by, be
import allure

@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Frunzelen')
@allure.description('Тест с использованием лямбда шагов allure')
@allure.feature('Поиск issues в Github')
@allure.link('https://github.com', name='Testing')
def test_github_lambda_steps():
    with allure.step("Открываем в браузере главную страницу сайта github"):
        browser.open("/")

    with allure.step("Ищем репозиторий eroshenkoam/allure-example"):
        browser.element(".search-input").click()
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
        browser.element("#query-builder-test").submit()

    with allure.step("Переходим в найденный репозиторий"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("В табе переходим в issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие issues с номером #65"):
        browser.element(by.partial_text("#65")).should(be.visible)

    with allure.step("Закрываем браузер"):
        browser.quit()