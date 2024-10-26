import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.smoketest
def test_google_send_keys(browser):
    browser.get("https://www.google.com")
    time.sleep(3)
    assert 'Google' == browser.title
    assert 'https://www.google.com/' == browser.current_url
    browser.find_element(By.ID, 'APjFqb').send_keys("dodge daytona ev" + Keys.ENTER)
    time.sleep(3)
    assert 'dodge daytona ev - Google Search' == browser.title
    assert 'dodge+daytona+ev' in browser.current_url
