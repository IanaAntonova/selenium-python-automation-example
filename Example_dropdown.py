import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.maximize_window()

browser.get("https://alhymrecords.com/")
time.sleep(7)
browser.find_element(By.LINK_TEXT, "EVENTS").click()
time.sleep(3)

artists_dropdown = Select(browser.find_element(By.ID, "artists_filter"))
artists_dropdown.select_by_visible_text("DJ Capital")
time.sleep(3)