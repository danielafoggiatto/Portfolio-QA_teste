import conftest
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class CarrinhoPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.botao_continuar_compras = (By.ID, "continue-shopping")

    def verificar_produto_carrinho_existe(self, nome_produto):
        produto = (self.item_inventario[0], self.item_inventario[1].format(nome_produto))
        self.verificar_se_elemento_existe(produto)

    def continuar_compras(self):
        self.clicar(self.botao_continuar_compras)