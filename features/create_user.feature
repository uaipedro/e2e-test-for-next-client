# language: pt
Funcionalidade: Cadastro de Usuário

Cenario: Criar user com sucesso
        Dado que estou na pagina de cadastro
        Quando eu faço singup com "usuario", "email" e "senha" novos
            """
            {
                "usuario": "novo_usuario",
                "email": "novo@usuario.com",
                "senha": "nova_senha"
            }
            """
        Então devo ser direcionado para a tela de login

Cenario: Criar user com email já cadastrado
        Dado que estou na pagina de cadastro
        Quando eu faço singup com um email já utilizado
        Então devo ver a mensagem "email já cadastrado"

Cenario: Criar user sem usuario
        Dado que estou na pagina de cadastro
        Quando eu faço singup sem informar usuario(username)
        Então devo ver a mensagem de erro no campo usuario(username)

Cenario: Criar user sem email
        Dado que estou na pagina de cadastro
        Quando eu faço singup sem informar email(email)
        Então devo ver a mensagem de erro no campo email(email)

Cenario: Criar user sem senha
        Dado que estou na pagina de cadastro
        Quando eu faço singup sem informar senha(password)
        Então devo ver a mensagem de erro no campo senha(password)

Cenario: Criar user com senha menor que 8 caracteres
        Dado que estou na pagina de cadastro
        Quando eu faço eu faço singup com senha(password) menor que 8 caracteres
        Então devo ver a mensagem de erro no campo senha(password)

Cenario: Criar user com username menor que 3 caracteres
        Dado que estou na pagina de cadastro
        Quando eu faço eu faço singup com usuario(username) menor que 3 caracteres
        Então devo ver a mensagem de erro no campo usuario(username)