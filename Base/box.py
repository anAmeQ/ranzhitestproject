from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

class Base():

    def __init__(self, browser):
        if browser == 'chrome' or browser == 'c':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox' or browser == 'f':
            self.driver = webdriver.Firefox()
        elif browser == 'ie' or browser == 'i':
            self.driver = webdriver.Ie()
        else: 
            raise Exception("输入的浏览器不合法")
    
    def open_url(self, url):
        self.driver.get(url)

    def get_element(self, selector, index=None):
        selector_key = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if index is None:
            if selector == 'id' or selector_key == 'i':
                element = self.driver.find_element(By.ID, selector_value)
            elif selector == 'name' or selector_key == 'n':
                element = self.driver.find_element(By.NAME, selector_value)
            elif selector == 'class name' or selector_key == 'c':
                element = self.driver.find_element(By.CLASS_NAME, selector_value)
            elif selector == 'tag name' or selector_key == 't':
                element = self.driver.find_element(By.TAG_NAME, selector_value)
            elif selector == 'link text' or selector_key == 'l':
                element = self.driver.find_element(By.LINK_TEXT, selector_value)
            elif selector == 'partical link text' or selector_key == 'p':
                element = self.driver.find_element(By.PARTIAL_LINK_TEXT, selector_value)
            elif selector == 'xpath' or selector_key == 'x':
                element = self.driver.find_element(By.XPATH, selector_value)
            elif selector == 'css selector' or selector_key == 's':
                element = self.driver.find_element(By.CSS_SELECTOR, selector_value)
            else:
                raise Exception("你输入的参数不合法")          
        elif index is not None:
            if selector == 'id' or selector_key == 'i':
                element = self.driver.find_elements(By.ID, selector_value)[index]
            elif selector == 'name' or selector_key == 'n':
                element = self.driver.find_elements(By.NAME, selector_value)[index]
            elif selector == 'class name' or selector_key == 'c':
                element = self.driver.find_elements(By.CLASS_NAME, selector_value)[index]
            elif selector == 'tag name' or selector_key == 't':
                element = self.driver.find_elements(By.TAG_NAME, selector_value)[index]
            elif selector == 'link text' or selector_key == 'l':
                element = self.driver.find_elements(By.LINK_TEXT, selector_value)[index]
            elif selector == 'partical link text' or selector_key == 'p':
                element = self.driver.find_elements(By.PARTIAL_LINK_TEXT, selector_value)[index]
            elif selector == 'xpath' or selector_key == 'x':
                element = self.driver.find_elements(By.XPATH, selector_value)[index]
            elif selector == 'css selector' or selector_key == 's':
                element = self.driver.find_elements(By.CSS_SELECTOR, selector_value)[index]
            else:
                raise Exception("你输入的参数不合法")
        else:
            raise Exception("你输入的参数不合法")

        return element

    def select_by_index(self, selector, index, elementindex=None):
        element = self.get_element(selector,elementindex)
        Select(element).select_by_index(index)

    def select_by_value(self, selector, value, elementindex=None):
        element = self.get_element(selector, elementindex)
        Select(element).select_by_value(value)

    def select_by_visible_text(self, selector, text, elementindex=None):
        element = self.get_element(selector, elementindex)
        Select(element).select_by_visible_text(text)

    def sleep(self, second):
        sleep(second)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


class BasePage():

    def __init__(self, driver:Base):
        self.driver = driver




if __name__ == "__main__":
    driver = Base('c')
    driver.open_url('https://www.baidu.com')
    driver.get_element('i,kw').send_keys('123455')
    driver.get_element('i,su').click()
    

