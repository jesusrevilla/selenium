import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class MyPageCategory(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.FirefoxOptions()
        # options.add_argument(--headless)
        self.driver = webdriver.Firefox(options=options)

    def test_select_options(self):
        driver = self.driver
        driver.get("https://jesusrevilla.github.io/wpproject0/contact.html")
        select = Select(driver.find_element_by_id("inputGroupSelect01"))
        select.select_by_value('4')
        element = driver.find_element_by_id("inputGroupSelect01")
        option = element.find_element_by_xpath('//*[@id="inputGroupSelect01"]/option[4]')
        self.assertEqual("Dashboard", option.get_attribute("text"))

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
