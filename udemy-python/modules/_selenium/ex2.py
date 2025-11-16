import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.get("https://google.com")

# Abrindo uma nova aba 
driver.execute_script('window.open("https://pt.wikipedia.org/wiki/Austr%C3%A1lia");')


# Obter todas as abas abertas
# É uma lista com todas as abas 
abas = driver.window_handles

time.sleep(5)

# Mudar de aba
driver.switch_to.window(abas[1])

# Scroollar até elemento desejad
historia =  driver.find_element(By.XPATH, '//*[@id="História"]')
driver.execute_script('arguments[0].scrollIntoView()', historia)

time.sleep(6)

# Fechar navegador 
driver.quit()

