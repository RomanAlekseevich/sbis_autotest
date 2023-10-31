import pytest

from pages.tensor.main_page import MainPage as TensorMainPage
from pages.sbis.main_page import MainPage as SbisMainPage
from pages.sbis.contacts_page import ContactsPage
from pages.sbis.downloads import DownloadsPage


@pytest.fixture
def tensor_main_page(driver):
    yield TensorMainPage(driver)
    
    
@pytest.fixture
def sbis_main_page(driver):
    yield SbisMainPage(driver)
    

@pytest.fixture
def downloads_page(driver):
    yield DownloadsPage(driver)
    
    
@pytest.fixture
def contacts_page(driver):
    yield ContactsPage(driver)
