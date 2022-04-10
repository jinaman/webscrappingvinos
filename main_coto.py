from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from mainPage_coto import MainPageCoto
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Vinos(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_vinostintos_coto(self):
        self.driver.get('https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-bebidas-bebidas-con-alcohol-vinos-vinos-tintos/_/N-1sad76x?Nf')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.pagina_principal = MainPageCoto(self.driver)
        time.sleep(10)

        """LOCATORS VINOS TINTOS COTO"""
        listadeprecios = self.pagina_principal.lista_de_precios()
        listadenombres = self.pagina_principal.lista_de_nombres()

        listadenombres2 = []
        for i in listadenombres:
            listadenombres2.append(i.text)

        precios2 = []
        for i in listadeprecios:
            precios2.append(i.text)

        while True:
            try:
                self.pagina_principal.click_mostrar_mas()
                time.sleep(5)
                listadeprecios = self.pagina_principal.lista_de_precios()
                listadenombres = self.pagina_principal.lista_de_nombres()
                for i in listadenombres:
                    listadenombres2.append(i.text)
                for i in listadeprecios:
                    precios2.append(i.text)

            except:
                time.sleep(5)
                break

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
        print(f'los nombres de los vinos tintos totales son {largo_nombres}')
        print(f'los precios de los vinos tintos totales son {largo_precios}')

        """MANEJO DE EXCEL"""
        filename='preciosdevinos2.csv'
        f = open(filename, 'a', encoding='utf-8')
        f.write('Vinos tintos - Coto,Precio')

        contador = 0
        for i in range(len(listadenombres2)):
            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + listanombrespunto[contador] + ',' + listapreciospuntos[contador])
                contador = contador + 1
            except:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + listanombrespunto[contador])
                contador = contador + 1

    def test_vinosblancos_coto(self):
        self.driver.get('https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-bebidas-bebidas-con-alcohol-vinos-vinos-blancos/_/N-1l5slhl?Nf')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.pagina_principal = MainPageCoto(self.driver)
        time.sleep(10)

        """LOCATORS VINOS BLANCOS COTO"""
        listadeprecios = self.pagina_principal.lista_de_precios()
        listadenombres = self.pagina_principal.lista_de_nombres()

        listadenombres2 = []
        for i in listadenombres:
            listadenombres2.append(i.text)

        precios2 = []
        for i in listadeprecios:
            precios2.append(i.text)

        while True:
            try:
                self.pagina_principal.click_mostrar_mas()
                time.sleep(5)
                listadeprecios = self.pagina_principal.lista_de_precios()
                listadenombres = self.pagina_principal.lista_de_nombres()
                for i in listadenombres:
                    listadenombres2.append(i.text)
                for i in listadeprecios:
                    precios2.append(i.text)

            except:
                time.sleep(5)
                break

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
        print(f'los nombres de los vinos blancos totales son {largo_nombres}')
        print(f'los precios de los vinos blancos totales son {largo_precios}')

        """MANEJO DE EXCEL"""
        filename='preciosdevinos2.csv'
        f = open(filename, 'a', encoding='utf-8')
        f.write('\n' +'Vinos blancos - Coto,Precio')

        contador = 0
        for i in range(len(listadenombres2)):
            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + listanombrespunto[contador] + ',' + listapreciospuntos[contador])
                contador = contador + 1
            except:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + listanombrespunto[contador])
                contador = contador + 1

    def test_vinosrosados_coto(self):
        self.driver.get('https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-bebidas-bebidas-con-alcohol-vinos-vinos-rosados/_/N-vrxj9f?Nf')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.pagina_principal = MainPageCoto(self.driver)
        time.sleep(10)

        """LOCATORS VINOS ROSADOS COTO"""
        listadeprecios = self.pagina_principal.lista_de_precios()
        listadenombres = self.pagina_principal.lista_de_nombres()

        listadenombres2 = []
        for i in listadenombres:
            listadenombres2.append(i.text)

        precios2 = []
        for i in listadeprecios:
            precios2.append(i.text)

        while True:
            try:
                self.pagina_principal.click_mostrar_mas()
                time.sleep(5)
                listadeprecios = self.pagina_principal.lista_de_precios()
                listadenombres = self.pagina_principal.lista_de_nombres()
                for i in listadenombres:
                    listadenombres2.append(i.text)
                for i in listadeprecios:
                    precios2.append(i.text)

            except:
                time.sleep(5)
                break

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
        print(f'los nombres de los vinos rosados totales son {largo_nombres}')
        print(f'los precios de los vinos rosados totales son {largo_precios}')

        """MANEJO DE EXCEL"""
        filename='preciosdevinos2.csv'
        f = open(filename, 'a', encoding='utf-8')
        f.write('\n' +'Vinos rosados - Coto,Precio')

        contador = 0
        for i in range(len(listadenombres2)):
            try:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + listanombrespunto[contador] + ',' + listapreciospuntos[contador])
                contador = contador + 1
            except:
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.pagina_principal.precios))
                f.write('\n' + listanombrespunto[contador])
                contador = contador + 1


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
