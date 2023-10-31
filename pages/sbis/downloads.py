import os
import re

from pages.base.base_page import BasePage
from pages.base.button import Button
from pages.base.link import Link
from config import BASE_DIR


class DownloadsPage(BasePage):
   def __init__(self, web_driver) -> None:
      super().__init__(web_driver)
      self.tab_button = Button(web_driver, "кнопка навигации", xpath='//div[@class="sbis_ru-VerticalTabs__left"]/div[@name="TabButtons"]//div[text()="{text}"]')
      self.link_download = Link(web_driver, "Ссылка на скачивание плагина", xpath='//h3[@class="sbis_ru-DownloadNew-h3"][contains(text(), "{text}")]/parent::div/following-sibling::div//a[contains(@class, "sbis_ru-DownloadNew-loadLink__link")]')


   def download_plugin(self, distr_type):
      file_name = re.split(r'/', self.link_download.get_attribute(attribute="href", text=distr_type))
      file_path = os.path.join(BASE_DIR,"tests", file_name[-1])
      
      if os.path.isfile(file_path):
         os.remove(file_path)
        
      self.link_download.click(text=distr_type)
      self.wait_page_loaded()
      self.wait_downloads_all()
    
      file_size = round((os.path.getsize(file_path))/1048576, 2)
      
      return file_path, file_size
   
   
   def check_file_size_downloaded_plugin(self, distr_type):
      size = re.findall(r'[0-9]+\.[0-9]+', self.link_download.get_text(text=distr_type))
      size = float(size[0])
      file_name = re.split(r'/', self.link_download.get_attribute(attribute="href", text=distr_type))
      file_path = os.path.join(BASE_DIR,"tests", file_name[-1])
      
      if os.path.isfile(file_path):
         file_size = round((os.path.getsize(file_path))/1048576, 2)
         assert file_size == size, "Вес файла не совпадает с указаным на сайте"
      else: 
         raise Exception(f"Отсутвует файл по пути: {file_path}")
       