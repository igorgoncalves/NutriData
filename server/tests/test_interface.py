# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait


# def test_alteracao_titulo():
  
#   # Cria instacia do navegador 
#   firefox = webdriver.Firefox()
  
#   # Acessa um link
#   firefox.get('http://localhost:4000')

#   # Espera eventos para execução
#   input_localidade = WebDriverWait(firefox, 10).until(
#       lambda firefox : firefox.find_element_by_css_selector('[aria-label="Localidade"]')
#     )

#   # Envio de ações de teclado
#   input_localidade.send_keys("Aracaju")
#   input_localidade.send_keys(Keys.ENTER)
  
#   titulo_alterado = firefox.find_element_by_class_name('step-2').get_attribute('textContent')
  
#   # Fechar navegador
#   firefox.quit()

#   assert titulo_alterado == '2º - Clique em um indicador de: Aracaju'

