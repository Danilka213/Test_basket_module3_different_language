import pytest
from selenium import webdriver
import time
import math
   
   
class TestMainPage1(): 
    #@pytest.fixture
    def test_check_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com//catalogue/coders-at-work_207/"
        browser.get(link)
        browser.implicitly_wait(10)
        assert browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"), "Button 'basket' absent"
        time.sleep(7)
