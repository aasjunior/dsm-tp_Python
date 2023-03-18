import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_path = 'C:\\Python311\\webdrivers\\chromium\\chromedriver.exe'
brave_path = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

service = Service(executable_path=chromedriver_path)
option = webdriver.ChromeOptions()
option.binary_location = brave_path

navegador = webdriver.Chrome(service=service, options=option)

tabela = pd.read_excel('Emitir.xlsx')

navegador.get("https://forms.office.com/r/kqAY0SyG49")

for i, cpf in enumerate(tabela["CPF"]):
    email = tabela.loc[i, "Email"]
    descricao = tabela.loc[i, "Descrição"]
    valor = tabela.loc[i, "Valor"]
    
    #preencher CPF
    navegador.find_element(By.XPATH, '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[1]/div/div[3]/div/span/input').send_keys(cpf)

    #preencher Email
    navegador.find_element(By.XPATH, '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/span/input').send_keys(email)

    #preencher Descrição
    navegador.find_element(By.XPATH, '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/span/textarea').send_keys(descricao)

    #preencher Valor
    navegador.find_element(By.XPATH, '//*[@id="cover-page-root"]/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/span/input').send_keys(str(valor))

    #clicar no botão
    navegador.find_element(By.XPATH, '//*[@id="cover-page-root"]/div[1]/div[2]/div[4]/div[1]/button/div').click()
    
    time.sleep(1)
    
    navegador.find_element(By.XPATH, '//*[@id="form-main-content"]/div[1]/div[2]/div[2]/div[2]/a').click()
    
navegador.quit()