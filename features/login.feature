#language: pt
Funcionalidade: Login

    

    Cenario: Login com sucesso
        Dado que eu tenho um usuário cadastrado
        Quando eu faço login com "email" e "senha"
            """
            {
                "email": "usuario@cadastrado.com",
                "senha": "senha123"
            }
            """
        Então devo ver mensagem de boas vindas que contenha "bem vind"