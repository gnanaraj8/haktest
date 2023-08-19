from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager 
import pytest
from locators import locator

class Demo:
    @pytest.fixture()
    def __init__(self,url):
        self.url=url
        self.driver.implicitly_wait(10)
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        pass
    def login(self):
        self.driver.find_element(by=By.XPATH, value=Regs.reg).click()
        self.driver.find_element(by=By.NAME, value=Reg.male).click()
        self.driver.find_element(by=By.NAME, value=Regs.first).send_keys("you")
        self.driver.find_element(by=By.NAME, value=Regs.last).send_keys("me")
        display=self.driver.find_element(by=By.XPATH, value=Regs.date)
        display_dropdown=Select(display)
        display_dropdown.select_by_value("12")
        display=self.driver.find_element(by=By.XPATH, value=Regs.month)
        display_dropdown=Select(display)
        display_dropdown.select_by_value("4")
        display=self.driver.find_element(by=By.XPATH, value=Regs.year)
        display_dropdown=Select(display)
        display_dropdown.select_by_value("1982")
        self.driver.find_element(by=By.NAME, value=Regs.email).send_keys("nothing@example.com")
        self.driver.find_element(by=By.NAME, value=Regs.company).send_keys("world")
        self.driver.find_element(by=By.NAME, value=Regs.pas).send_keys("gsdhgfsdkf")
        self.driver.find_element(by=By.NAME, value=Regs.con_pass).send_keys("gsdhfsdkf")
        self.driver.find_element(by=By.NAME, value=Regs.regis).click
    def categories(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.XPATH, value=Computer.computer_locator).click()
        self.driver.find_element(by=By.XPATH, value=computer.desktop_locator).click()
        self.driver.find_element(by=By.XPATH, value=Computer.notebook_locator).click()
        self.driver.file_element(by=By.XPATH, Value=Computer.soft_locator).click()
        
        assert self.driver.title=="nopcommerce"
        print("passed")
url="https://demo.nopcommerce.com/"        
d=Demo()
d.login()
d.categories()          