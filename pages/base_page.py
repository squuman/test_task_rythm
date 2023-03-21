from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BasePage:
    base_url: str
    _driver: webdriver.Chrome

    def __init__(self, driver):
        self._driver = driver

    def find_element(self, locator, time=10):
        """
        Поиска элемента

        :param locator:
        :param time:
        :return:
        """
        return WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """
        Поиск списка элементов

        :param locator:
        :param time:
        :return:
        """
        return WebDriverWait(self._driver, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        """
        Переход на страницу
        :return:
        """
        self._driver.get(self.base_url)
        delay = 3

        try:
            WebDriverWait(self._driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            print('Page was loaded')
        except TimeoutException:
            print("Loading took too much time")

    def is_visible(self, locator) -> bool:
        """
        Проверка видимости элемента

        :param locator:
        :return:
        """
        element = self._driver.find_element(locator)

        if element.is_displayed():
            return True
        else:
            return False
