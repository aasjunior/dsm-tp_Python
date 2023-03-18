from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_path = 'C:\\Python311\\webdrivers\\chromium\\chromedriver.exe'
brave_path = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

service = Service(executable_path=chromedriver_path)
option = webdriver.ChromeOptions()
option.binary_location = brave_path

navegador = webdriver.Chrome(service=service, options=option)

navegador.get("https://forms.office.com/r/kqAY0SyG49")

#preencher CPF
navegador.find_element(By.XPATH, '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[1]/div/div[3]/div/span/input').send_keys('11111111111')

#preencher Email
navegador.find_element(By.XPATH, '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/span/input').send_keys('email@email.com')

#preencher Descrição
navegador.find_element(By.XPATH, '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/span/textarea').send_keys('Curso de Python')

#preencher Valor
navegador.find_element(By.XPATH, '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/span/input').send_keys('3000')

#clicar no botão
navegador.find_element(By.XPATH, '//*[@id="cover-page-root"]/div[1]/div[2]/div[4]/div[1]/button/div').click()