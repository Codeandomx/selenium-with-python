#!/usr/bin/python

# Importamos las librerias necesarias
from include.Driver import Driver


def test():
    # Creamos una instancia del driver
    driver = Driver()

    # Obtenemos el driver
    # d = driver.getDriverFirefox(False)
    d = driver.getDriverChrome(False)

    # Obtenemos la siguiente url
    d.get('http://google.com')

    # Esperamos 5 segundos
    d.implicitly_wait(5)

    # Obtenemos el titulo de la pagina
    print("Page Title is : %s" %d.title)

    # cerramos el driver
    d.quit()


if __name__ == "__main__":
    test()