from pages.base.base_page import BasePage
from pages.base.link import Link


class Header(BasePage):
    def __init__(self, web_driver) -> None:
        super().__init__(web_driver)
        self.contacts = Link(web_driver, "Контакты", xpath='//div[@class="sbisru-Header"]//a[contains(@href, "contacts")]')
        