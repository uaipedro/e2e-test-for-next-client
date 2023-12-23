# language: pt
Funcionalidade: Cadastro de Usuário

Cenario: Criar user com sucesso
        Dado que eu tenho um usuário não cadastrado e estou na pagina de cadastro
        Quando eu faço singup com "usuario", "email" e "senha"
            """
            {
                "usuario": "novo_usuario",
                "email": "novo@usuario.com",
                "senha": "nova_senha"
            }
            """
        Então devo ser direcionado para a tela de login