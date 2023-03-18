from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get("https://brave.com/pt-br/")
##navegador.find_element("xpath", '/html/body/header/div/button').click()
navegador.find_element("xpath", '//*[@id="home-download-button-hero"]').click()
