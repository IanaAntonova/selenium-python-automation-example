import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("search_item",
                         [
                             "Xbox",
                             "Jewlery",
                             "Playstation",
                             "Books"
                         ])
@pytest.mark.iana_test
def test_ebay_multiple_search(browser, search_item):
    browser.get("https://www.ebay.com/")
    browser.find_element(By.ID, "gh-ac").send_keys(search_item + Keys.ENTER)
    assert search_item + " for sale | eBay" == browser.title



