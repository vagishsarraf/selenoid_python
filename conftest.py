import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")


@pytest.fixture
def test_remote(request):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")


@pytest.fixture
def test_local(request):
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # driver.get("https://the-internet.herokuapp.com/upload")

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")