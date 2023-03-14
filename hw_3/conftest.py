import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture(scope="session", autouse=True)
def get_url():
    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com/')
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def wait(get_url):
    wait = WebDriverWait(get_url, timeout=10)
    return wait


