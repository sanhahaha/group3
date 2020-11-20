

class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_member_manager(self):

        self.driver.find_element_by_link_text(u'会员管理')

    def click_logout(self):
        pass

    def click_sale(self):
        pass