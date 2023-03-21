from pages import BasePage
from elements import MainPageElements


class MainPage(BasePage):
    base_url = 'https://demoqa.com/'

    def click_on_elements(self):
        button_element = self.find_element(MainPageElements.button_element)
        button_element.click()
