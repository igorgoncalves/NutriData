import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException 


def get_titulo (login, password):
  # Cria instacia do navegador 
  firefox = webdriver.Firefox()
  
#   # Acessa um link
#   firefox.get('http://localhost:4000')

  # Espera eventos para execução
  btn_admin = WebDriverWait(firefox, 10).until(
    lambda firefox : firefox.find_element_by_css_selector('.v-toolbar__items .v-btn')
  )

  btn_admin.click()

  input_login = WebDriverWait(firefox, 10).until(
    lambda firefox : firefox.find_element_by_css_selector('[name="login"]')
  )

  input_login.send_keys(login)

  input_senha = firefox.find_element_by_css_selector('[name="password"]')

  input_senha.send_keys(password)

  btn_login = WebDriverWait(firefox, 10).until(
    lambda firefox : firefox.find_element_by_css_selector('.v-btn')
  )
  btn_login.click()
  
  try:
    titulo = WebDriverWait(firefox, 10).until(
      lambda firefox : firefox.find_element_by_css_selector('h2').get_attribute('textContent')
    )  
  finally:
    firefox.quit()
  # Fechar navegador
  firefox.quit()
  return titulo


def test_login_sucesso():
  titulo = get_titulo("admin", "admin")
  assert titulo == 'Lista de macroindicadores'

def test_login_falha():  
  with pytest.raises(TimeoutException):    
    assert get_titulo("admin", "batata")