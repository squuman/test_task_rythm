import allure

from pages import MainPage
from pages import ElementsPage


@allure.story("Проверка открытия главной страницы")
def test_open_main_page(browser):
    """
    Проверяем открывается ли главная страница

    :param browser:
    :return:
    """
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(browser)
        main_page.go_to_site()
    with allure.step("Проверка открытия страницы с помощью заголовка страницы"):
        assert browser.title is not None


@allure.story("Проверка открытия страницы элементов")
def test_open_elements_page(browser):
    """
    Проверяем открывается ли страница elements при клике на elements

    :param browser:
    :return:
    """
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(browser)
        main_page.go_to_site()
    with allure.step("Нажатие на Elements"):
        main_page.click_on_elements()
    with allure.step("Проверка открытия страницы Elements"):
        assert browser.title is not None


@allure.story("Проверка нажатия на checkbox")
def test_click_button_checkbox(browser):
    """
    Проверка нажатия на элементв checkbox в списке элементов

    :param browser:
    :return:
    """
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(browser)
        main_page.go_to_site()
    with allure.step("Нажатие на Elements"):
        main_page.click_on_elements()
    with allure.step("Нажатие на Check Box"):
        elements_page = ElementsPage(browser)
        elements_page.click_on_check_box()
    with allure.step("Проверка, что нажатие на Check Box вызвало открытие общей директории"):
        assert elements_page.check_checkbox_is_opened()


@allure.story("Проверка нажатия на директорию Home")
def test_click_on_home_toggle(browser):
    """
    Проверка нажатия на директорию home

    :param browser:
    :return:
    """
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(browser)
        main_page.go_to_site()
    with allure.step("Нажатие на Elements"):
        main_page.click_on_elements()
    with allure.step("Нажатие на Check Box"):
        elements_page = ElementsPage(browser)
        elements_page.click_on_check_box()
    with allure.step("Нажатие на директорию Home"):
        elements_page.click_on_home_toggle()
    with allure.step("Проверка, что директория Home раскрыта"):
        assert elements_page.check_home_toggle_is_opened()


@allure.story("Проверка нажатия на директорию Downloads")
def test_click_on_downloads_toggle(browser):
    """
    Проверка нажатия на директорию downloads

    :param browser:
    :return:
    """
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(browser)
        main_page.go_to_site()
    with allure.step("Нажатие на Elements"):
        main_page.click_on_elements()
    with allure.step("Нажатие на Check Box"):
        elements_page = ElementsPage(browser)
        elements_page.click_on_check_box()
    with allure.step("Нажатие на директорию Home"):
        elements_page.click_on_home_toggle()
    with allure.step("Нажатие на директорию Download"):
        elements_page.click_on_downloads_toggle()
    with allure.step("Проверка, что директория Downloads раскрыта"):
        assert elements_page.check_downloads_toggle_is_opened()


@allure.story("Проверка нажатия на чекбокс Word File.doc")
def test_choose_word_file(browser):
    """
    Проверка открытия директории HOME

    :param browser:
    :return:
    """
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(browser)
        main_page.go_to_site()
    with allure.step("Нажатие на Elements"):
        main_page.click_on_elements()
    with allure.step("Нажатие на Check Box"):
        elements_page = ElementsPage(browser)
        elements_page.click_on_check_box()
    with allure.step("Нажатие на директорию Home"):
        elements_page.click_on_home_toggle()
    with allure.step("Нажатие на директорию Download"):
        elements_page.click_on_downloads_toggle()
    with allure.step("Нажатие на чекбокс Word File.doc"):
        elements_page.click_on_checkbox_wordfile()
    with allure.step("Проверка вывода результата"):
        assert "You have selected: wordFile" == elements_page.get_result_text()
