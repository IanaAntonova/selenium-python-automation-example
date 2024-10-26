import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.regressiontest
def test_ebay_search(browser):

    browser.get('https://www.ebay.com/')
    assert "Electronics, Cars, Fashion, Collectibles & More | eBay" == browser.title
    assert "https://www.ebay.com/" == browser.current_url
    browser.find_element(By.ID, "gh-ac").send_keys("Lexus" + Keys.ENTER)
    select_car = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(browser.find_element(By.XPATH, '//span[@role="heading"] [@aria-level="3"] [text() = "2012 Lexus LS460L AWD"]')))
    select_car.click()

