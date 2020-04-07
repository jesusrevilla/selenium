import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class PythonOrgSearch(unittest.TestCase):

    def setUp(self) -> None:
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No result found" not in driver.page_soure

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
