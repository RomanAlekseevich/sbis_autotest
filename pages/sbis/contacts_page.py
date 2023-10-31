from pages.base.base_page import BasePage
from pages.base.link import Link
from pages.base.text import Text
from pages.base.list import List
from pages.base.list_item import ListItem


class ContactsPage(BasePage):

    def __init__(self, web_driver) -> None:
        super().__init__(web_driver)
        self.banner_tensor = Link(web_driver, "Банер Тензор", xpath='//div[@id="contacts_clients"]//a[@title="tensor.ru"]')
        self.region_chooser = Text(web_driver, "Регион пользователя", xpath='//div[@class="sbisru-Contacts"]//span[contains(@class, "sbis_ru-Region-Chooser__text")][contains(text(),"{region}")]')
        self.contacts_clients_list = List(web_driver, "Список партнёров", xpath= '//div[@id="contacts_clients"]//div[@data-qa="list"]')
        self.contacts_clients_item = ListItem(web_driver, "Элементы списка партнёров", xpath='//div[@id="contacts_clients"]//div[@data-qa="item"][contains(.,"{text}")]')
        self.region_chooser_list_item = ListItem(web_driver, "Регион для выбора из списка", xpath='//div[@class="sbis_ru-Region-Panel__container"]/ul/li/span[contains(@title, "{region}")]/parent::li')
    
    @property
    def contacts_clients_items_amount(self) -> int:
        items_amount = len(self.contacts_clients_item.get_presence_all_elements(text=""))
        return items_amount
        