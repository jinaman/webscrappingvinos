from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    def __init__(self, my_driver):
        self.driver =my_driver
        self.close_alert_button = (By.XPATH, '//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]')
        self.mostrar_mas_boton = (By.XPATH, "//button[@class='vtex-button bw1 ba fw5 v-mid relative pa0 lh-solid br2 min-h-small t-action--small bg-action-primary b--action-primary c-on-action-primary hover-bg-action-primary hover-b--action-primary hover-c-on-action-primary pointer ']/div[contains(text(),'Mostrar más')]")
        self.listadenombres = (By.XPATH, '//span[@class="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body"]')
        self.precios = (By.XPATH, '//span[@class="lyracons-dynamic-weight-price-0-x-textPriceUnit"]')#(By.XPATH, '//span[@class="lyracons-carrefourarg-product-price-1-x-sellingPriceValue"]') #(By.XPATH, '//span[@class="lyracons-dynamic-weight-price-0-x-textPriceUnit"]')

    def lista_de_nombres(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.listadenombres))
        return self.driver.find_elements(*self.listadenombres)

    def lista_de_precios(self):
        return self.driver.find_elements(*self.precios)

    def cerrar_alerta_cookies(self):
        self.driver.find_element(*self.close_alert_button).click()

    def click_mostrar_mas(self):
        self.driver.find_element(*self.mostrar_mas_boton).click()

    def mostrar_todas_las_paginas(self):
        while True:
            try:
                WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_element_located(self.mostrar_mas_boton))
                self.click_mostrar_mas()
                #time.sleep(5)
            except:
                #time.sleep(5)
                break










