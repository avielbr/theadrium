# functions for interacting with elements on the screen on the basis
# of their respective HTML identifiers (ID, Name, CSS...)


class Touchers:
    def __init__(self, driver):
        self.driver = driver

    def fill_by_id(self, id, text):
        self.driver.find_element_by_id(id).send_keys(text)

    def click_by_id(self, id):
        self.driver.find_element_by_id(id).click()

    def click_by_name(self, name):
        self.driver.find_element_by_name(name).click()

    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def find_by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

