from pages.sbis.main_page import MainPage as SbisMainPage
from pages.sbis.contacts_page import ContactsPage


def test_S02(sbis_main_page: SbisMainPage, contacts_page: ContactsPage):
    sbis_main_page.get("https://sbis.ru/")
    sbis_main_page.header.contacts.click()
    assert contacts_page.region_chooser.should_be_visible(region="Ярославская обл."),\
        "Регион не отображается или отббражается регион с неверным значением"
    assert contacts_page.contacts_clients_list.should_be_visible(),\
        "Список партнёров не отображается"
    assert contacts_page.contacts_clients_items_amount > 1,\
        "Колличество партнёров в списке меньше одного"
    list1 = contacts_page.contacts_clients_item.get_presence_all_elements(text='')
    contacts_page.region_chooser.click(region="Ярославская обл.")
    contacts_page.region_chooser_list_item.click(region="Камчатский край")
    contacts_page.wait_page_loaded()
    list2 = contacts_page.contacts_clients_item.get_presence_all_elements(text='')
    assert contacts_page.region_chooser.should_be_visible(region="Камчатский край"),\
        "Регион не отображается или отббражается регион с неверным значением"
    assert contacts_page.contacts_clients_list.should_be_visible(),\
        "Список партнёров не отображается"
    assert contacts_page.contacts_clients_items_amount > 1,\
        "Колличество партнёров в списке меньше одного"
    assert "41-kamchatskij-kraj" in contacts_page.current_url, "URL не соответствует выбраному региону"
    assert "Камчатский край" in contacts_page.title, "Title не соответсвует выбраному региону"
    assert list2 != list1, "Список партнёров не изменился"
