
# 🧪 Portfólio de Testes Automatizados - QA

Este repositório contém meus estudos e práticas de **automação de testes** utilizando **Python, Selenium e Pytest**.  
O objetivo é demonstrar habilidades em **testes funcionais, UI e validações automáticas** em diferentes aplicações web.

---

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **Pytest** (estrutura de testes)
- **Selenium WebDriver** (automação de navegador)
- **Applitools** (validação visual)
- **VS Code** (IDE)

---

## 📂 Estrutura do Repositório
- **AppliTools** → Testes de login com validação visual  
- **AutomationExercise** → Cadastro e login na plataforma AutomationExercise  
- **DEMOQA** → Testes funcionais (alertas, formulários, upload/download)  
- **Outros_Testes** → Exemplos de waits (implícito, explícito), dropdowns, iframes e interações  
- **SauceDemo** → Fluxo completo de login, adicionar produtos ao carrinho e finalizar compra  

---

## 🔧 Como Executar os Testes
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/QA_TESTE.git
````

2. Acesse a pasta do projeto:

   ```bash
   cd QA_TESTE
   ```
3. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```
4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```
5. Execute os testes com Pytest:

   ```bash
   pytest -v
   ```

---

## 📝 Exemplos de Testes

### 🔹 Login Válido (SauceDemo)

```python
def test_login_valido(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "products" in driver.current_url
```

### 🔹 Cadastro (AutomationExercise)

```python
def test_cadastro_usuario(driver):
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    driver.find_element(By.NAME, "name").send_keys("Teste")
    driver.find_element(By.NAME, "email").send_keys("teste@mail.com")
    driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
    assert "Enter Account Information" in driver.page_source
```

---

## 🎯 Objetivo

Este portfólio tem como objetivo **demonstrar conhecimentos práticos em QA Automation**, cobrindo:

* Boas práticas de automação
* Estrutura organizada de testes
* Diferentes tipos de validação (UI, waits, formulários, fluxos de compra)

---

## 📌 Autor

👩‍💻 Desenvolvido por **Daniela Foggiatto**
📎 [LinkedIn](https://www.linkedin.com/in/danielafoggiatto)
📎 [GitHub](https://github.com/danielafoggiatto)

```
