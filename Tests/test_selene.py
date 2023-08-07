import allure
from allure_commons.types import Severity
from selene import browser, by, be

@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Frunzelen')
@allure.description('Тест без использования разметки allure')
@allure.feature('Поиск issues в Github')
@allure.link('https://github.com', name='Testing')
def test_github():
    browser.open("/")
    browser.element(".search-input").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#65")).should(be.visible)

    browser.quit()