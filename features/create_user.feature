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