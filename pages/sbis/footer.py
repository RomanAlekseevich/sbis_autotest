from pages.base.base_page import BasePage
from pages.base.list_item import ListItem


class Footer(BasePage):
    def __init__(self, web_driver) -> None:
        super().__init__(web_driver)
        self.sitemap_list_item = ListItem(web_driver, "Пункт карты сайта", xpath='//li[@class="sbisru-Footer__list-item"]/a[contains(text(), "{text}")]') 
        