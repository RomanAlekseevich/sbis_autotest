from pages.base.base_page import BasePage
from pages.base.text import Text
from pages.base.link import Link
from pages.base.image import Image


class MainPage(BasePage):

    def __init__(self, web_driver) -> None:
        super().__init__(web_driver)
        self.banner_title = Text(web_driver, "Баннер, заголовок", xpath='//p[contains(@class, "tensor_ru-Index__card-title")][contains(text(), "{title}")]')
        self.banner_link = Link(web_driver, "Ссылка подробнее на банере", xpath='//p[contains(.,"{title}")]/following-sibling::p/a')
        self.work_banner_images = Image(web_driver, "Картинки на банере 'Работаем'", xpath='//img[contains(@class, "tensor_ru-About__block3-image")]') 
    
    
    def work_banner_images_should_have_correct_sizes(self):
        sizes = self.work_banner_images.get_sizes()
        if sizes:
            width_list = []
            heidth_list = []
            for iter in sizes:
                width_list.append(iter[0])
                heidth_list.append(iter[1])
            if len(set(width_list))>1 or len(set(heidth_list))>1:
                return False
            else:
                return True
        