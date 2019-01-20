# importamos la libreria
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def getChrome():
    # Opciones necesarias para no mostrar utilidades de chrome
    options = Options()
    options.add_argument("--no-sandbox") #This make Chromium reachable
    options.add_argument("--no-default-browser-check") #Overrides default choices
    options.add_argument("--no-first-run")
    options.add_argument("--disable-default-apps") 
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    # Vamos al sitio web
    driver.get("http://www.google.com")

    driver.implicitly_wait(5) # sleep for 10 seconds

    print("Page Title is : %s" %driver.title)

    # cerramos el driver
    driver.quit()


if __name__ == "__main__":
    getChrome()
