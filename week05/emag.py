from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pandas as pd

browser = webdriver.Edge(EdgeChromiumDriverManager().install())
browser.get("https://www.emag.ro/#opensearch")
get_element = browser.find_element_by_id('searchboxTrigger')
get_element.send_keys("telefon")
get_element.submit()
browser.close()