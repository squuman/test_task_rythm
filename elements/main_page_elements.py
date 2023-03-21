from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class MainPageElements:
    button_element = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]')
