from Base.box import Base, BasePage
from Page.login import Login


class AddMember(BasePage):

    def add_member(self, account, realname, dept, role, password1, 
                    password2, email):
            
        self.driver.get_element('')
