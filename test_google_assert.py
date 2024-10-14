import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.smoketest
def test_google_assert(browser):
    
    browser.get("https://www.google.com")
    time.sleep(3)
    assert 'Google' == browser.title
    assert 'https://www.google.com/' == browser.current_url



