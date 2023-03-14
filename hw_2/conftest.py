import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.get('https://courses.letskodeit.com/practice')
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def wait(browser):
    wait = WebDriverWait(browser, timeout=10)
    return wait

def a():
    pass