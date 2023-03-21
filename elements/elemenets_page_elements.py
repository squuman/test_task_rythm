from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class ElementsPageElements:
    button_check_box = (By.XPATH, '//li[@id="item-1"]')
    button_open_home_directory = (By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]')
    button_open_downloads_directory = (
        By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/ol/li/ol/li[3]/span/button')
    button_download_wordfile_checkbox = (
        By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]')

    dropdown_menu_from_home = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/ol/li/ol')
    dropdown_menu_from_downloads = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/ol/li/ol/li[3]/ol')
    tree_wrapper = (By.XPATH, '//div[@class="check-box-tree-wrapper"]')
    result = (By.XPATH, '//div[@id="result"]')
