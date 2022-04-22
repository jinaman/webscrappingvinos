from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPageChangomas:
    def __init__(self, my_driver):
        self.driver =my_driver
        self.siguiente_pagina = (By.XPATH, "//div[contains(text(),'Mostrar más')]")
        self.listadenombres = (By.XPATH, '//h1[@class="vtex-product-summary-2-x-productNameContainer mv0 vtex-product-summary-2-x-nameWrapper overflow-hidden c-on-base f5"]')#//div[@class="descrip_full"]')
        self.precios = (By.XPATH, '//div[@class="vtex-store-components-3-x-sellingPrice vtex-store-components-3-x-sellingPriceContainer pv1 b c-on-base vtex-store-components-3-x-price_sellingPriceContainer"]')#(By.XPATH, '//span[@class="lyracons-carrefourarg-product-price-1-x-sellingPriceValue"]') #(By.XPATH, '//span[@class="lyracons-dynamic-weight-price-0-x-textPriceUnit"]')

    def lista_de_nombres(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.listadenombres))
        return self.driver.find_elements(*self.listadenombres)

    def lista_de_precios(self):
        return self.driver.find_elements(*self.precios)

    def click_mostrar_mas(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.siguiente_pagina))
        self.driver.find_element(*self.siguiente_pagina).click()

    def mostrar_todas_las_paginas(self):
        while True:
            try:
                WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located(self.siguiente_pagina))
                self.click_mostrar_mas()
                #time.sleep(5)
            except:
                #time.sleep(5)
                break




