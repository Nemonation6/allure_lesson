import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag('critical')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Авторизованный пользователь не может создать задачу в репозитории')
    allure.dynamic.label('https://github.com')
    pass

@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'D')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_decorator_labels():
    pass