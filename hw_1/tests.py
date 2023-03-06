from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def launch_browser(browser):
    if browser == 'firefox':
        browser = webdriver.Firefox()
        browser.get("https://www.demoblaze.com/")
    elif browser == 'edge':
        browser = webdriver.Edge()
        browser.get("https://www.demoblaze.com/")
    browser.quit()


launch_browser('firefox')
launch_browser('edge')


def locate_element_by_xpath(element):
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")
    try:
        element = driver.find_element(By.XPATH, element)
        element.is_displayed()
        print("Element is located")
    except NoSuchElementException:
        print('No Such element')


locate_element_by_xpath('//*[@id="navbarExample"]/ul/li[1]/a')
locate_element_by_xpath('//*[@id="navbarExample"]/ul/li[2]/a')
locate_element_by_xpath('//*[@id="navbarExample"]/ul/li[3]/a')
locate_element_by_xpath('//*[@id="navbarExample"]/ul/li[4]/a')
locate_element_by_xpath('//*[@id="navbarExample"]/ul/li[5]/a')
locate_element_by_xpath('//*[@id="logout2"]')


def locate_element_by_css_selector(element):
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")

    try:
        element = driver.find_element(By.CSS_SELECTOR, element)
        element.is_displayed()
        print("Element is located")
    except NoSuchElementException:
        print("No Such element")


locate_element_by_css_selector('div.list-group>:nth-child(2)')
locate_element_by_css_selector('div.list-group>:nth-child(3)')
locate_element_by_css_selector('div.list-group>:nth-child(4)')


def find_highest_priced_item():
    browser = webdriver.Chrome()
    browser.get("https://www.demoblaze.com/")
    wait = WebDriverWait(browser, timeout=10)
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div.card")))

    items = browser.find_elements(By.CSS_SELECTOR, "div.card")

    max_price = 0
    item_with_max_price = ''

    for item in items:
        price_element = item.find_element(By.CSS_SELECTOR, "div.card-block > h5")
        name_element = item.find_element(By.CSS_SELECTOR, "div.card-block > h4")

        price_text = price_element.text
        price = int(price_text.strip('$'))

        if price > max_price:
            max_price = price
            item_with_max_price = name_element.text

    return f"The highest priced item is, {item_with_max_price}, and the price is: ${max_price}"


print(find_highest_priced_item())


class TestCase:

    def wait_for_list_len(self, browser, locator, exp_len, timeout=10):
        WebDriverWait(browser, timeout).until(
            lambda driver: len(driver.find_elements(*locator)) == exp_len
        )

    def test_case(self):
        driver = webdriver.Chrome()
        driver.get("https://www.demoblaze.com/")

        phones = driver.find_element(By.CSS_SELECTOR, "div.list-group>:nth-child(2)")
        phones.click()
        self.wait_for_list_len(driver, (By.CSS_SELECTOR, '#tbodyid>div'), 7)
        phone_items = driver.find_elements(By.CSS_SELECTOR, "h4.card-title")
        assert len(phone_items) == 7

        laptops = driver.find_element(By.CSS_SELECTOR, "div.list-group>:nth-child(3)")
        laptops.click()
        self.wait_for_list_len(driver, (By.CSS_SELECTOR, '#tbodyid>div'), 6)
        laptop_items = driver.find_elements(By.CSS_SELECTOR, "h4.card-title")
        assert len(laptop_items) == 6

        monitors_link = driver.find_element(By.CSS_SELECTOR, "div.list-group>:nth-child(4)")
        monitors_link.click()
        self.wait_for_list_len(driver, (By.CSS_SELECTOR, '#tbodyid>div'), 2)
        monitor_items = driver.find_elements(By.CSS_SELECTOR, "h4.card-title")
        assert len(monitor_items) == 2

        driver.quit()


test_case = TestCase()
test_case.test_case()
