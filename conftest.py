"""
Файл с фикстурами
"""
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome(executable_path='./drivers/')
    yield driver
    driver.quit()
