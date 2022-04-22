from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from mainPage_carrefour import MainPage
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime



class Vinos(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.now = datetime.now()
        current_date = self.now.strftime("%d_%m_%Y-%H")#_%M_%S")
        self.filename = f'{current_date}.csv'


    def test_a_vinostintos_carrefour(self):
        self.driver.get('https://www.carrefour.com.ar/Bebidas/Vinos/Vinos-tintos')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.pagina_principal = MainPage(self.driver)
        time.sleep(10)
        self.pagina_principal.cerrar_alerta_cookies()
        time.sleep(10)
        self.pagina_principal.mostrar_todas_las_paginas()
        time.sleep(5)

        """LOCATORS VINOS TINTOS CARREFOUR"""
        listadeprecios = self.pagina_principal.lista_de_precios()
        listadenombres = self.pagina_principal.lista_de_nombres()

        listadenombres2 = []
        for i in listadenombres:
            listadenombres2.append(i.text)  # Con esto lleno la lista de nombres 2
        # print(listadenombres2)  # LISTA DE NOMBRES LLENA

        precios2 = []
        for i in listadeprecios:
            precios2.append(i.text)  # LISTA DE PRECIO LLENA
        # print(precios2)

        largo_nombres = len(listadenombres2)
        largo_precios = len(precios2)
        print('\n' + f'los nombres de los vinos tintos totales son {largo_nombres}')
        print(f'los precios de los vinos tintos totales son {largo_precios}')

        """MANEJO DE EXCEL"""
        # filename = 'preciosdevinos.csv'
        f = open(self.filename, 'a', encoding='utf-8')
        f.write('Supermercado,Vinos tintos - Carefour,Precio')  # Los headees del excel

        contador = 0
        for i in range(len(listadenombres2)):
            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + 'Carrefour' + ',' +listadenombres2[contador] + ',' + precios2[contador])
                contador = contador + 1
            except:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + 'Carrefour' + ',' +listadenombres2[contador])
                contador = contador + 1

    def test_b_vinos_blancos_carrefour(self):
        self.driver.get('https://www.carrefour.com.ar/Bebidas/Vinos/Vinos-blancos')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.pagina_principal = MainPage(self.driver)
        time.sleep(10)
        self.pagina_principal.cerrar_alerta_cookies()
        time.sleep(10)
        time.sleep(5)
        self.pagina_principal.mostrar_todas_las_paginas()

        """LOCATORS VINOS BLANCOS CARREFOUR"""
        listadeprecios = self.pagina_principal.lista_de_precios()
        listadenombres = self.pagina_principal.lista_de_nombres()

        listadenombres3 = []
        for i in listadenombres:
            listadenombres3.append(i.text)
        # print(listadenombres3)

        precios3 = []
        for i in listadeprecios:
            precios3.append(i.text)
        # print(precios3)

        largo_nombres = len(listadenombres3)
        largo_precios = len(precios3)
        print('\n' + f'los nombres de los vinos blancos totales son {largo_nombres}')
        print(f'los precios de los vinos blancos totales son {largo_precios}')

        """MANEJO DE EXCEL"""
        #filename = 'preciosdevinos.csv'
        f = open(self.filename, 'a', encoding='utf-8')
        f.write('\n' + 'Supermercado,Vinos blancos - Carefour,Precio')

        contador = 0
        for i in range(len(listadenombres3)):
            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + 'Carrefour' + ',' +listadenombres3[contador] + ',' + precios3[contador])
                contador = contador + 1
            except:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + 'Carrefour' + ',' +listadenombres3[contador])
                contador = contador + 1

    def test_c_vinos_rosados_carrefour(self):
        self.driver.get('https://www.carrefour.com.ar/Bebidas/Vinos/Vinos-rosados')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.pagina_principal = MainPage(self.driver)
        time.sleep(10)
        self.pagina_principal.cerrar_alerta_cookies()
        time.sleep(10)
        self.pagina_principal.mostrar_todas_las_paginas()
        time.sleep(5)

        """LOCATORS VINOS ROSADOS CARREFOUR"""
        listadeprecios = self.pagina_principal.lista_de_precios()
        listadenombres = self.pagina_principal.lista_de_nombres()

        listadenombres4 = []
        for i in listadenombres:
            listadenombres4.append(i.text)
        # print(listadenombres4)

        precios4 = []
        for i in listadeprecios:
            precios4.append(i.text)
        # print(precios4)

        largo_nombres = len(listadenombres4)
        largo_precios = len(precios4)
        print('\n' + f'los nombres de los vinos rosados totales son {largo_nombres}')
        print(f'los precios de los vinos rosados totales son {largo_precios}')

        """MANEJO DE EXCEL"""
        #filename = 'preciosdevinos.csv'
        f = open(self.filename, 'a', encoding='utf-8')
        f.write('\n' + 'Supermercado,Vinos rosados - Carefour,Precio')

        contador = 0
        for i in range(len(listadenombres4)):
            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + 'Carrefour' + ',' +listadenombres4[contador] + ',' + precios4[contador])
                contador = contador + 1
            except:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + 'Carrefour' + ',' +listadenombres4[contador])
                contador = contador + 1

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
