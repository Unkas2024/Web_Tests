import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser():
    pass
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
