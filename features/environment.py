# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.create_user_page import CreateUserPage


def before_all(context):
    # selenium 4

    context.driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

    user = dict(
        email="usuario@cadastrado.com",
        usuario="usuario",
        senha="senha123",
    )

    context.pre_created_user = user

    page = CreateUserPage(context.driver)
    page.load()
    page.fill_form(**user)
    page.submit_form()
    now = time.time()
    while time.time() - now < 5:
        if (
            "https://next-client-with-login.vercel.app/login"
            in context.driver.current_url
            or "username already" in page.get_error_message()
        ):
            return

    import ipdb

    ipdb.sset_trace()


def before_scenario(context, scenario):
    # context.driver.maximize_window()
    ...


def before_step(context, step):
    context.driver.implicitly_wait(7)


def after_all(context):
    context.driver.quit()
