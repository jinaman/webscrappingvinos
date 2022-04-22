from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from mainPage_changomas import MainPageChangomas
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


    def test_a_vinostintos_changomas(self):
        self.driver.get('https://www.masonline.com.ar/vinos-y-espumantes/vino-tinto')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.pagina_principal = MainPageChangomas(self.driver)
        time.sleep(10)
        self.pagina_principal.mostrar_todas_las_paginas()
        """LOCATORS VINOS TINTOS CHANGO MAS"""
        listadeprecios = self.pagina_principal.lista_de_precios()
        listadenombres = self.pagina_principal.lista_de_nombres()

        listadenombres2 = []
        for i in listadenombres:
            listadenombres2.append(i.text)

        precios2 = []
        for i in listadeprecios:
            precios2.append(i.text)

        listanombrespunto = []
        for i in listadenombres2:
            nue = []
            for letra in i:
                if letra == ',':
                    letra = '.'
                nue.append(letra)
            sentence = ''
            for word in nue:
                sentence += str(word)
            listanombrespunto.append(sentence)

        listapreciospuntos = []
        for i in precios2:
            nue = []
            for letra in i:
                if letra == ',':
                    letra = '.'
                nue.append(letra)
            sentence = ''
            for word in nue:
                sentence += str(word)
            listapreciospuntos.append(sentence)

        largo_nombres = len(listanombrespunto)
        largo_precios = len(listapreciospuntos)
        print('\n' + f'los nombres de los vinos tintos totales son {largo_nombres}')
        print(f'los precios de los vinos tintos totales son {largo_precios}')

        """MANEJO DE EXCEL"""
        # current_date = self.now.strftime("%d_%m_%Y-%H")#_%M_%S")
        # filename = f'{current_date}.csv'
        f = open(self.filename, 'a', encoding='utf-8')
        f.write('Supermercado,Vinos tintos - Chango mas,Precio')

        contador = 0
        for i in range(len(listadenombres2)):
            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + 'Changomas' + ',' + listanombrespunto[contador] + ',' + listapreciospuntos[contador])
                contador = contador + 1
            except:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + 'Changomas' + ',' + listanombrespunto[contador])
                contador = contador + 1

    def test_b_vinosblancos_changomas(self):
        self.driver.get('https://www.masonline.com.ar/vinos-y-espumantes/vino-blanco')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.pagina_principal = MainPageChangomas(self.driver)
        time.sleep(10)
        self.pagina_principal.mostrar_todas_las_paginas()

        """LOCATORS VINOS BLANCOS CHANGO MAS"""
        listadeprecios = self.pagina_principal.lista_de_precios()
        listadenombres = self.pagina_principal.lista_de_nombres()

        listadenombres2 = []
        for i in listadenombres:
            listadenombres2.append(i.text)

        precios2 = []
        for i in listadeprecios:
            precios2.append(i.text)

        listanombrespunto = []
        for i in listadenombres2:
            nue = []
            for letra in i:
                if letra == ',':
                    letra = '.'
                nue.append(letra)
            sentence = ''
            for word in nue:
                sentence += str(word)
            listanombrespunto.append(sentence)

        listapreciospuntos = []
        for i in precios2:
            nue = []
            for letra in i:
                if letra == ',':
                    letra = '.'
                nue.append(letra)
            sentence = ''
            for word in nue:
                sentence += str(word)
            listapreciospuntos.append(sentence)

        largo_nombres = len(listanombrespunto)
        largo_precios = len(listapreciospuntos)
        print('\n' + f'los nombres de los vinos blancos totales son {largo_nombres}')
        print(f'los precios de los vinos blancos totales son {largo_precios}')

        """MANEJO DE EXCEL"""
        # current_date = self.now.strftime("%d_%m_%Y-%H")#_%M_%S")
        # filename = f'{current_date}.csv'
        f = open(self.filename, 'a', encoding='utf-8')
        f.write('\n' + 'Supermercado,Vinos blancos - Chango mas,Precio')

        contador = 0
        for i in range(len(listadenombres2)):
            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + 'Changomas' + ',' + listanombrespunto[contador] + ',' + listapreciospuntos[contador])
                contador = contador + 1
            except:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + 'Changomas' + ',' + listanombrespunto[contador])
                contador = contador + 1

    def test_c_vinosrosados_changomas(self):
        self.driver.get('https://www.masonline.com.ar/vinos-y-espumantes/vino-rosado')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.pagina_principal = MainPageChangomas(self.driver)
        time.sleep(10)
        self.pagina_principal.mostrar_todas_las_paginas()

        """LOCATORS VINOS ROSADOS CHANGO MAS"""
        listadeprecios = self.pagina_principal.lista_de_precios()
        listadenombres = self.pagina_principal.lista_de_nombres()

        listadenombres2 = []
        for i in listadenombres:
            listadenombres2.append(i.text)

        precios2 = []
        for i in listadeprecios:
            precios2.append(i.text)

        listanombrespunto = []
        for i in listadenombres2:
            nue = []
            for letra in i:
                if letra == ',':
                    letra = '.'
                nue.append(letra)
            sentence = ''
            for word in nue:
                sentence += str(word)
            listanombrespunto.append(sentence)

        listapreciospuntos = []
        for i in precios2:
            nue = []
            for letra in i:
                if letra == ',':
                    letra = '.'
                nue.append(letra)
            sentence = ''
            for word in nue:
                sentence += str(word)
            listapreciospuntos.append(sentence)

        largo_nombres = len(listanombrespunto)
        largo_precios = len(listapreciospuntos)
        print('\n' + f'los nombres de los vinos rosados totales son {largo_nombres}')
        print(f'los precios de los vinos rosados totales son {largo_precios}')

        """MANEJO DE EXCEL"""
        # current_date = self.now.strftime("%d_%m_%Y-%H")#_%M_%S")
        # filename = f'{current_date}.csv'
        f = open(self.filename, 'a', encoding='utf-8')
        f.write('\n' + 'Supermercado,Vinos blancos - Chango mas,Precio')

        contador = 0
        for i in range(len(listadenombres2)):
            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + 'Changomas' + ',' + listanombrespunto[contador] + ',' + listapreciospuntos[contador])
                contador = contador + 1
            except:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + 'Changomas' + ',' + listanombrespunto[contador])
                contador = contador + 1


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
