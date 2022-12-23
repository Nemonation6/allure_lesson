import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open("https://github.com")

    with allure.step('Ищем репозиторий'):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Открываем таб Issue'):
        s("#issues-tab").click()

    with allure.step('Проверяем наличие Issue с номером 76'):
        s(by.partial_text("#76")).should(be.visible)


def test_decorator_tests():
    open_main_page()
    search_for_repository()
    go_to_repo()
    open_issue_tab()
    should_see_issue_with_number('#76')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open("https://github.com")


@allure.step('Ищем репозиторий')
def search_for_repository():
    s(".header-search-input").click()
    s(".header-search-input").send_keys("eroshenkoam/allure-example")
    s(".header-search-input").submit()


@allure.step('Переходим по ссылке репозитория')
def go_to_repo():
    s(by.link_text("eroshenkoam/allure-example")).click()


@allure.step('Открываем таб Issue')
def open_issue_tab():
    s("#issues-tab").click()


@allure.step('Проверяем наличие Issue с номером 76')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()