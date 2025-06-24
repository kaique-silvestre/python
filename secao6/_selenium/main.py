import pathlib

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.commom.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 

from time import sleep



ROOT_FOLDER = pathlib.Path(__file__).parent 
CHROMEDRIVER_EXE = ROOT_FOLDER / 'drivers' / 'chromedriver.exe' 


chrome_option = webdriver.ChromeOptions() # Configuarações que vamos passar
chrome_service = Service(executable_path=CHROMEDRIVER_EXE) # Qual serviço vai utilizar o chromedriver
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_option
)



chrome_browser.get('https://google.com.br')

search_input = WebDriverWait(chrome_browser, 10).until(
    expected_conditions.presence_of_element_located(
        By.ID, 'input'
    )
)

search_input.send_keys("Hello World!")

