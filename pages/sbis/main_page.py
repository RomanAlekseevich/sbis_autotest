from pages.base.base_page import BasePage
from pages.sbis.header import Header
from pages.sbis.footer import Footer
from pages.base.button import Button

class MainPage(BasePage):

    def __init__(self, web_driver) -> None:
        super().__init__(web_driver)
        self.header = Header(web_driver)
        self.footer = Footer(web_driver)
        self.close_cookie = Button(web_driver, "Кнопка закрать сообщение cookie", xpath='//div[@class="sbis_ru-CookieAgreement__close"]')
