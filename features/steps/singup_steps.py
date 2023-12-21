import time
from json import loads

from behave import given, then, when


@given("que eu tenho um usuário não cadastrado e estou na pagina de cadastro")
def step_given_que_eu_estou_na_pagina_de_cadastro(context):
    # Implemente a lógica para navegar até a página de cadastro
    context.driver.get("https://next-client-with-login.vercel.app/singin")
    pass


@when('eu faço singup com "usuario", "email" e "senha"')
def step_when_eu_preencho_o_formulario_de_cadastro(context):
    # Implemente a lógica para preencher o formulário de cadastro com o email, senha e confirmação de senha fornecidos
    texto = loads(context.text)
    context.driver.find_element("id", "username").send_keys(texto["usuario"])
    context.driver.find_element("id", "email").send_keys(texto["email"])
    context.driver.find_element("id", "password").send_keys(texto["senha"])
    context.driver.find_element("id", "confirmPassword").send_keys(texto["senha"])
    context.driver.find_element("xpath", "//button[@type='submit']").click()
    pass


@then("devo ser direcionado para a tela de login")
def step_then_devo_ser_direcionado_para_tela_login(context):
    # Implemente a lógica para verificar se a mensagem de cadastro bem-sucedido é exibida
    # assert if the url changes to login
    # wait for the page to load

    time.sleep(2)

    assert (
        context.driver.current_url == "https://next-client-with-login.vercel.app/login"
    )
    pass
