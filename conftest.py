import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config import BASE_DIR


@pytest.fixture
def sbis_chrome_options():
    
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": f"{BASE_DIR}/tests/",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    return options

@pytest.fixture
def driver(sbis_chrome_options):
    
    driver = webdriver.Chrome(options=sbis_chrome_options, 
                              service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()
    