import conftest
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.adicionar_carrinho = (By.XPATH, "//*[text()= 'Add to cart']")
        self.icone_carrinho = (By.XPATH, "//*[@class='shopping_cart_link']")


    def verificar_login_realizado_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)
        assert self.encontrar_elemento(self.titulo_pagina).text == "Products", "Login não realizado com sucesso."

    def adicionar_produto_ao_carrinho(self, nome_produto):
        produto = (self.item_inventario[0], self.item_inventario[1].format(nome_produto))
        self.clicar(produto)
        self.clicar(self.adicionar_carrinho)
    
    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)

    
        