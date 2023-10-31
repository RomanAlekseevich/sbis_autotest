import allure

from abc import ABC, abstractmethod
from typing import Any
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class Component(ABC):
    def __init__(self, web_driver, name: str, **kwargs) -> None:
        self.web_driver = web_driver
        self.name = name
        for attr in kwargs:
            self.locator = (str(attr).replace('_', ' '), str(kwargs.get(attr)))
       
        
    @property
    @abstractmethod
    def type_of(self) -> str:
        return 'component'
    
    
    def get_locator(self, **kwargs) -> str:
        locator = (self.locator[0],self.locator[1].format(**kwargs))
        return locator
    
    
    def wait_to_be_clickable(self, **kwargs):
        """ Wait until the element will be ready for click. """

        element = None
        locator = self.get_locator(**kwargs)
        try:
            element = WebDriverWait(self.web_driver, timeout=30).until(
                EC.element_to_be_clickable(locator)
            )
        except:
            print('Element not clickable!')

        return element
    
    
    def get_presence_element(self, **kwargs):
        
        element = None
        locator = self.get_locator(**kwargs)
        try:
            element = WebDriverWait(self.web_driver, timeout=30).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print('Is not presence')

        return element
    
    
    def get_presence_all_elements(self, **kwargs):
        
        element = None
        locator = self.get_locator(**kwargs)
        try:
            element = WebDriverWait(self.web_driver, timeout=30).until(
                EC.presence_of_all_elements_located(locator)
            )
        except:
            print('Are not presence')

        return element
    
    
    def send_enter(self, **kwargs):
        element = self.get_presence_element(**kwargs)
        action = ActionChains(self.web_driver)
        action.send_keys_to_element(element, Keys.ENTER).perform()


    def should_be_visible(self, **kwargs):
        
        element = self.get_presence_element(**kwargs)
        
        if element:
            return element.is_displayed()

        return False
    
    def get_attribute(self, attribute, **kwargs):
        
        element = self.get_presence_element(**kwargs)
        
        if element:
            return element.get_attribute(attribute)
        
        return False
    
    def get_text(self, **kwargs):
        element = self.get_presence_element(**kwargs)
        
        if element:
            return str(element.text)
        
        return False
    
    
    def click(self, hold_seconds=0, x_offset=1, y_offset=1, delta_x=0, delta_y=0, **kwargs):
        """ Wait and click the element. """

        element = self.wait_to_be_clickable(**kwargs)

        if element:
            action = ActionChains(self.web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).\
                    scroll_by_amount(delta_x, delta_y).\
                    pause(hold_seconds).click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self.locator))



        