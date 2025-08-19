import pytest
from Pages.login_page import LoginPage
from Pages.home_page import HomePage

@pytest.mark.login
@pytest.mark.usefixtures("setup_teardown")

class TestCT03:
    def test_ct03_login_senha_invalida(self):
        mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"

        login_page = LoginPage()
        login_page.fazer_login("standard_user", "senha_incorreta")
        login_page.verificar_mensagem_erro_login_existe()
        login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperada)

