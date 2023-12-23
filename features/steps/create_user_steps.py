import time
from json import loads

from behave import given, then, when

from pages.create_user_page import CreateUserPage


@given("que estou na pagina de cadastro")
def step_given_que_eu_estou_na_pagina_de_cadastro(context):
    context.page = CreateUserPage(context.driver)
    context.page.load()
    pass


@when('eu faço singup com "usuario", "email" e "senha" novos')
def step_when_eu_preencho_o_formulario_de_cadastro(context):
    # Implemente a lógica para preencher o formulário de cadastro com o email, senha e confirmação de senha fornecidos
    texto = loads(context.text)
    indice_unico = str(int(time.time()) % 100000)
    usuario = texto["usuario"] + indice_unico
    email = (
        texto["email"].split("@")[0] + indice_unico + "@" + texto["email"].split("@")[1]
    )
    senha = texto["senha"]
    context.page.fill_form(email=email, usuario=usuario, senha=senha)
    context.page.submit_form()
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


@when("eu faço singup com um email já utilizado")
def step_when_eu_faco_login_com_email_e_senha_cadastrados(context):
    # Implemente a lógica para preencher o formulário de cadastro com o email, senha e confirmação de senha fornecidos
    form_data = context.pre_created_user
    context.page.fill_form(**form_data)
    context.page.submit_form()
    pass


@then('devo ver a mensagem "email já cadastrado"')
def step_then_devo_ver_a_mensagem_email_ja_cadastrado(context):
    now = time.time()
    while (
        time.time() - now < 5
        and "username already" not in context.page.get_error_message()
    ):
        ...

    assert "username already" in context.page.get_error_message()
    pass
