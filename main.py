from selenium import webdriver
import unittest
from mainPage import MainPage
import time


class Vinos(unittest.TestCase):

    def test_vinosTintos(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.carrefour.com.ar/Bebidas/Vinos/Vinos-tintos')
        self.driver.implicitly_wait(5)
        self.pagina_principal = MainPage(self.driver)
        time.sleep(10)
        self.pagina_principal.cerrar_alerta_cookies()
        time.sleep(10)
        try:
            self.pagina_principal.click_mostrar_mas()
        except:
            print("No se clickeó el primer mostrar más")
        time.sleep(5)

        while self.pagina_principal.es_esta_la_ultima_pagina():
            self.pagina_principal.click_mostrar_mas()
            time.sleep(5)
        """Locators """
        listadenombres = self.driver.find_elements_by_xpath('//span[@class="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body"]')
        precios = self.driver.find_elements_by_xpath('//span[@class="lyracons-dynamic-weight-price-0-x-textPriceUnit"]')




        listadenombres2 = []
        for i in listadenombres:
            listadenombres2.append(i.text)      # Con esto lleno la lista de nombres 2
        print(listadenombres2)                 #LISTA DE NOMBRES LLENA

        precios2 = []
        for i in precios:
            precios2.append(i.text)            #LISTA DE PRECIO LLENA

        # MANEJO DE EXCEL

        filename='preciosdevinos.csv'
        f = open(filename, 'a', encoding='utf-8')
        f.write('Nombre,Precio')                                    #Los headees del excel

        largo_nombres = len(listadenombres2)
        largo_precios = len(precios2)
        print(f'los nombres totales son {largo_nombres}')
        print(f'los precios totales son {largo_precios}')

        contador = 0
        for i in range(len(listadenombres2)):
            f.write('\n' + listadenombres2[contador] + ',' + precios2[contador])
            contador = contador + 1

        """VINOS BLANCOS """

        self.driver.get('https://www.carrefour.com.ar/Bebidas/Vinos/Vinos-blancos')
        time.sleep(10)
        self.pagina_principal.cerrar_alerta_cookies()
        time.sleep(10)
        try:
            self.pagina_principal.click_mostrar_mas()
        except:
            print("No se clickeó el primer mostrar más")
        time.sleep(5)
        while self.pagina_principal.es_esta_la_ultima_pagina():
            self.pagina_principal.click_mostrar_mas()
            time.sleep(5)

        listadenombres3 = []
        for i in listadenombres:
            listadenombres3.append(i.text)      # Con esto lleno la lista de nombres 2
        print(listadenombres3)                 #LISTA DE NOMBRES LLENA

        precios3 = []
        for i in precios:
            precios3.append(i.text)            #LISTA DE PRECIO LLENA




        time.sleep(5)






    # def tearDown(self):
    #     self.driver.close()
    #     self.driver.quit()




