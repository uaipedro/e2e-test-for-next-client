# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def before_all(context):
    # selenium 4

    context.driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )


def before_scenario(context, scenario):
    # context.driver.maximize_window()
    ...


def before_step(context, step):
    context.driver.implicitly_wait(7)


def after_all(context):
    context.driver.quit()
