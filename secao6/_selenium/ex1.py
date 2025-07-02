from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# abrir o navegador
driver = webdriver.Chrome()

# Acessar o site
driver.get("https://youtube.com")

# colocar navegador em tela cheia
driver.maximize_window()

# selecionar um elemento
youtube_search = driver.find_element(By.CSS_SELECTOR, "#center > yt-searchbox > div.ytSearchboxComponentInputBox.ytSearchboxComponentInputBoxDark > form > input")

# Escrever 
youtube_search.send_keys("Hello")