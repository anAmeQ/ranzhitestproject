from Base.box import Base,BasePage

class Login(BasePage):

    def login(self, username, password):
        self.driver.open_url('http://localhost/ranzhi/www')
        self.driver.get_element('i,account').send_keys(username)
        self.driver.get_element('i,password').send_keys(password)
        self.driver.get_element('i,submit').click()



if __name__ == "__main__":
    chrome_driver = Base('c')
    Login(chrome_driver).login('admin', '123456')
    chrome_driver.sleep(3)
    chrome_driver.quit()

