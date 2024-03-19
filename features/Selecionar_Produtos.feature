Feature: Selecionar Produto 

    Scenario: selecionar produto "Sauce Labs Backpack"
        Given que acesso o site Sauce Demo
        When preenho os campos de login com usuario standard_user e senha secret_sauce
        Then sou direcionado para pagina Home
