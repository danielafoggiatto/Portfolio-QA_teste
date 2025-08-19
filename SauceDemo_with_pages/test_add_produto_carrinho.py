from selenium.webdriver.common.by import By
import pytest
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.carrinho_page import CarrinhoPage

@pytest.mark.carrinho
@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_add_produto_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        produto1 = "Sauce Labs Backpack"
        produto2 = "Sauce Labs Bolt T-Shirt"

        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.adicionar_produto_ao_carrinho(produto1)

        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto1)

        carrinho_page.continuar_compras()
        home_page.adicionar_produto_ao_carrinho(produto2)
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto2)

