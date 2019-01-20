# importamos la libreria
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def getFirefox():
    # For linux
    # from pyvirtualdisplay import Display
    # Creamos un entorno virtual
    # display = Display(visible=0,size=(1024,768))
    # display.start()

    # options = Options()
    # options.headless = True

    # Creamos una instancia
    # driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    # driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

    # Vamos al sitio web
    driver.get("http://www.google.com")

    driver.implicitly_wait(5) # sleep for 10 seconds

    print("Page Title is : %s" %driver.title)

    # cerramos el driver
    driver.quit()


if __name__ == "__main__":
    getFirefox()
