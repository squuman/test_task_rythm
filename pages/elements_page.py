from pages import BasePage
from elements import ElementsPageElements


class ElementsPage(BasePage):
    base_url = 'https://demoqa.com/elements'

    def click_on_check_box(self):
        button_check_box = self.find_element(ElementsPageElements.button_check_box)
        button_check_box.click()

    def click_on_home_toggle(self):
        button_open_home_directory = self.find_element(ElementsPageElements.button_open_home_directory)
        button_open_home_directory.click()

    def click_on_downloads_toggle(self):
        button_open_downloads_directory = self.find_element(ElementsPageElements.button_open_downloads_directory)
        button_open_downloads_directory.click()

    def click_on_checkbox_wordfile(self):
        button_download_wordfile_checkbox = self.find_element(ElementsPageElements.button_download_wordfile_checkbox)
        button_download_wordfile_checkbox.click()

    def check_checkbox_is_opened(self):
        if self.find_element(ElementsPageElements.tree_wrapper).is_displayed():
            return True
        else:
            return False

    def check_home_toggle_is_opened(self):
        if self.find_element(ElementsPageElements.dropdown_menu_from_home).is_displayed():
            return True
        else:
            return False

    def check_downloads_toggle_is_opened(self):
        if self.find_element(ElementsPageElements.dropdown_menu_from_downloads).is_displayed():
            return True
        else:
            return False

    def get_result_text(self):
        result = self.find_element(ElementsPageElements.result)

        return str(result.text).replace('\n', ' ')
