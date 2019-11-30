# importamos la libreria
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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

    # obtener estructura de la pagina
    html = driver.page_source
    print(html)

    # Ingresar texto en una pagina
    text_area = driver.find_element_by_id('textarea')
    text_area.send_keys("This text is send using Python code.")

    # Obtener los enlaces del sitio
    driver.get('https://www.w3.org/')
    for a in driver.find_elements_by_xpath('.//a'):
        print(a.get_attribute('href'))

    # cerramos el driver
    driver.quit()


if __name__ == "__main__":
    getChrome()
