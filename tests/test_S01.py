from pages.sbis.main_page import MainPage as SbisMainPage
from pages.sbis.contacts_page import ContactsPage
from pages.tensor.main_page import MainPage as TensorMainPage


def test_S01(sbis_main_page: SbisMainPage, contacts_page: ContactsPage, tensor_main_page: TensorMainPage):
    sbis_main_page.get('https://sbis.ru/')
    sbis_main_page.header.contacts.click()
    sbis_main_page.wait_page_loaded()
    contacts_page.banner_tensor.click()
    tensor_main_page.wait_page_loaded()
    tensor_main_page.switch_to_last_tab()
    tensor_main_page.wait_page_loaded()
    assert tensor_main_page.banner_title.should_be_visible(title="Сила в людях"), 'Эллемент "Сила в людях" не найдена'
    tensor_main_page.banner_link.click(delta_y=50, title="Сила в людях")
    tensor_main_page.wait_page_loaded()
    assert tensor_main_page.current_url == "https://tensor.ru/about", "Некорректнай URL"
    assert tensor_main_page.work_banner_images_should_have_correct_sizes(), "Отсутсвуют изибражения или некорректные размеры"
