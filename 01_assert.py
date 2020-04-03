"""
Recovered from https://selenium-python.readthedocs.io/getting-started.html#simple-usage
on 3 March 2020
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://wwww.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No result found." not in driver.page_source
driver.close()
