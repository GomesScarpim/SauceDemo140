from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    context.driver = webdriver.Chrome() # instanciar o Web Driver para o Chome
    context.driver.maximize_window # Maximizar janela do navegador
    context.driver.implicitly_wait # esperar até 10 segundos por qualquer elemento
    context.driver.get("https://www.saucedemo.com/") #abrir o navegador no endereço do site alvo

@when(u'preenho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario) # Digitar o Usuário
    context.driver.find_element(By.ID, "password").send_keys(senha) #Preencher a senha
    context.driver.find_element(By.ID, "login-button").click() #clicar no botao login

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    time.sleep(2)

    context.driver.quit()