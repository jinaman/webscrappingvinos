from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, my_driver):
        self.driver =my_driver
        self.nombre_del_vino = (By.XPATH, '//span[@class="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body"]')
        self.close_alert_button = (By.XPATH, '//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]')
        self.mostrar_mas_boton = (By.XPATH, "//button[@class='vtex-button bw1 ba fw5 v-mid relative pa0 lh-solid br2 min-h-small t-action--small bg-action-primary b--action-primary c-on-action-primary hover-bg-action-primary hover-b--action-primary hover-c-on-action-primary pointer ']/div[contains(text(),'Mostrar más')]")
        self.mensaje_fin_de_pagina = (By.XPATH, "//span[contains(text(),'Has visto los ')]")
        self.contenedor_de_precio = (By.XPATH, "//span[@class='lyracons-carrefourarg-product-price-1-x-sellingPriceValue']")
        self.integers = (By.XPATH, '//span[@class="lyracons-carrefourarg-product-price-1-x-currencyInteger"]')






    def obtener_nombre(self):
        return self.driver.find_element(*self.nombre_del_vino).text

    def get_names(self):
        return self.driver.find_elements(*self.nombre_del_vino)

    def cerrar_alerta_cookies(self):
        self.driver.find_element(*self.close_alert_button).click()

    def click_mostrar_mas(self):
        self.driver.find_element(*self.mostrar_mas_boton).click()

    def es_esta_la_ultima_pagina(self):
        try:
            self.driver.find_element(*self.mensaje_fin_de_pagina)
        except:
            return True
        return False








