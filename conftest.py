"""
Файл с фикстурами
"""
import os

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def chrome_options():
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    return options


def firefox_options():
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    return options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="default name")


@pytest.fixture(scope='session')
def browser(pytestconfig):
    browser_name = pytestconfig.getoption('browser')

    if browser_name == 'Chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options())
    elif browser_name == 'Firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise Exception("Unknown browser")

    yield driver
    driver.quit()
