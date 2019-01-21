#!/usr/bin/python

# importamos la libreria
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#Creamos el driver para trabajar con selenium
class Driver:
    # Constuctor
    def __init__(self):
        # Opciones
        self.options = Options()
        self.options.add_argument('--ignore-certificate-error')
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--ignore-certificate-error')
        # Logs
        self.service_args_chrome = ['--verbose', '--log-path=./chromedriver.log']


    def getDriverFirefox(self, view = True):
        if not view:
            # Ocultamos el navegador
            self.options.headless = True


        driver = webdriver.Firefox(options=self.options)

        return driver


    def getDriverChrome(self, view = True):
        if not view:
            # Ocultamos el navegador
            self.chrome_options.headless = True
            # Opciones para no mostrar herramientas de Chrome
            self.chrome_options.add_argument("--no-sandbox") # Corremos como root
            self.chrome_options.add_argument("--no-default-browser-check") #Overrides default choices
            self.chrome_options.add_argument("--no-first-run")
            self.chrome_options.add_argument("--disable-default-apps")
            
        
        # driver = webdriver.Chrome(options=self.options, service_args=self.service_args_chrome)
        driver = webdriver.Chrome(chrome_options=self.chrome_options)


        return driver


    def getDriverIE(self,view = True):
        if not view:
            # Ocultamos el navegador
            self.options.headless = True


        driver = webdriver.IE(options=self.options)

        return driver
