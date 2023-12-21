from behave import given, then, when


@given("que eu tenho um usuário cadastrado")
def step_given_que_eu_tenho_um_usuario_cadastrado(context):
    # Implemente a lógica para garantir que um usuário está cadastrado
    pass


@when('eu faço login com "{email}" e "{senha}"')
def step_when_eu_faco_login_com_email_e_senha(context, email, senha):
    # Implemente a lógica para fazer login com o email e senha fornecidos
    pass


@then("devo ver mensagem de boas vindas")
def step_then_devo_ver_mensagem_de_boas_vindas(context):
    # Implemente a lógica para verificar se a mensagem de boas-vindas é exibida
    pass
