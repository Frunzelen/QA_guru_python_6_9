from allure_commons.types import Severity
from selene import browser, by, be
import allure

@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Frunzelen')
@allure.description('Тест с использованием декоратора allure')
@allure.feature('Поиск issues в Github')
@allure.link('https://github.com', name='Testing')
def test_github_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#65")
    close_browser()

@allure.step("Открываем в браузере главную страницу сайта github")
def open_main_page():
    browser.open("/")

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element(".search-input").click()
    browser.element("#query-builder-test").send_keys(repo)
    browser.element("#query-builder-test").submit()

@allure.step("Переходим в найденный репозиторий {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()

@allure.step("В табе переходим в issues")
def open_issue_tab():
    browser.element("#issues-tab").click()

@allure.step("Проверяем наличие issues с номером {number}")
def should_see_issue_with_number(number):
        browser.element(by.partial_text(number)).should(be.visible)

@allure.step("Закрываем браузер")
def close_browser():
        browser.quit()