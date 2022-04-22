from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPageCoto:
    def __init__(self, my_driver):
        self.driver =my_driver
        self.siguiente_pagina = (By.XPATH, "//a[@title='Siguiente']")
        self.siguiente_pagina_2 = (By.XPATH, "//ul[@id='atg_store_pagination']//a[@class='disabledLink']//parent::li//following-sibling::li")
        self.listadenombres = (By.XPATH, '//span[@class="span_productName"]')#//div[@class="descrip_full"]')
        self.precios = (By.XPATH, '//div[@class="product_info_container"]/span[@class="unit"]')#(By.XPATH, '//span[@class="lyracons-carrefourarg-product-price-1-x-sellingPriceValue"]') #(By.XPATH, '//span[@class="lyracons-dynamic-weight-price-0-x-textPriceUnit"]')

    def lista_de_nombres(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.listadenombres))
        return self.driver.find_elements(*self.listadenombres)

    def lista_de_precios(self):
        return self.driver.find_elements(*self.precios)

    def click_mostrar_mas(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.siguiente_pagina))
            self.driver.find_element(*self.siguiente_pagina).click()
        except:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.siguiente_pagina_2))
            self.driver.find_element(*self.siguiente_pagina_2).click()
