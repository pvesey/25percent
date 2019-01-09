from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class selenium_tests(object):
    """docstring for selenium_tests."""
    def __init__(self, url):
        super(selenium_tests, self).__init__()
        self.arg = url
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def test_has_alert(self, arg):
        pass

    def screen_capture(self, filename, width, height):
        self.driver.set_window_size(width, height)
        self.driver.save_screenshot(filename)
        return

    def test_has_cookies(self):
        if len(self.driver.get_cookies())>0:
            return True
        else:
            return False

    def test_has_localStorage(self):
        if self.driver.execute_script("return window.localStorage.length;") > 0:
            return True
        else:
            return False

    def test_contact_page(self):
        try:
            input1 = self.driver.find_element_by_name('field1')
            input1.send_keys('Firstname Surname')
            input2 = self.driver.find_element_by_name('field2')
            input2.send_keys('name@email.com')
            input3 = self.driver.find_element_by_name('field3')
            input3.send_keys('This is a test Message')
            enterButton = self.driver.find_element_by_id('submit')
            enterButton.send_keys(Keys.ENTER)

        except Exception as e:
            print("contact form exception")

        return
