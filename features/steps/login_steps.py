import time
from json import loads
from unittest import TestCase

from behave import given, then, when


@given("que eu tenho um usuário cadastrado")
def step_given_que_eu_tenho_um_usuario_cadastrado(context):
    context.driver.get("https://next-client-with-login.vercel.app/")
    pass


@when('eu faço login com "{email}" e "{senha}"')
def step_when_eu_faco_login_com_email_e_senha(context, email, senha):
    texto = loads(context.text)
    context.driver.find_element("id", "email").send_keys(texto["email"])
    context.driver.find_element("id", "password").send_keys(texto["senha"])
    context.driver.find_element("xpath", "//button[@type='submit']").click()

    time.sleep(1)
    pass


@then("devo ver mensagem de boas vindas que contenha {message}")
def step_then_devo_ver_mensagem_de_boas_vindas(context, message):
    welcome_message = context.driver.find_element("xpath", "//h2").text.lower()
    TestCase().assertIn(message.lower().replace('"', ""), welcome_message)
    pass
