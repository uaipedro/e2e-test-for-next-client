#language: pt
Funcionalidade: Login

    Cenario: Criar user com sucesso
        Dado que eu tenho um usuário não cadastrado e estou na pagina de cadastro
        Quando eu faço singup com "usuario", "email" e "senha"
            """
            {
                "usuario": "usuario_valido_2",
                "email": "usuario@valido.co.br",
                "senha": "senha_valida"
            }
            """
        Então devo ser direcionado para a tela de login

    Cenario: Login com sucesso
        Dado que eu tenho um usuário cadastrado
        Quando eu faço login com "email" e "senha"
            """
            {
                "email": "email@valido.com",
                "senha": "senha_valida"
            }
            """
        Então devo ver mensagem de boas vindas que contenha "bem vind"