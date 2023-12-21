#language: pt
Funcionalidade: Login

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