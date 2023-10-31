import re
import os

from config import BASE_DIR

from pages.sbis.main_page import MainPage as SbisMainPage
from pages.sbis.downloads import DownloadsPage


def test_S03(sbis_main_page: SbisMainPage, downloads_page: DownloadsPage):
    sbis_main_page.get("https://sbis.ru/")
    sbis_main_page.wait_page_loaded()
    sbis_main_page.close_cookie.click()
    sbis_main_page.footer.sitemap_list_item.click(text="Скачать СБИС")
    sbis_main_page.wait_page_loaded()
    downloads_page.tab_button.click(text="СБИС Плагин")
    downloads_page.download_plugin(distr_type="Веб-установщик")
    downloads_page.check_file_size_downloaded_plugin(distr_type="Веб-установщик")
