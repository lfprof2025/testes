from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Caminho para o chromedriver
chrome_driver_path = r"C:\Drivers\chromedriver.exe"

# Inicializa o serviço do Chrome
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # 1. Acessa a página de cursos presenciais
    driver.get("https://unifil.br/presencial/")
    driver.maximize_window()
    time.sleep(3)

    # 2. Valida título da página
    assert "Presencial" in driver.title or "Unifil" in driver.title
    print("Página de cursos presenciais acessada com sucesso!")

    # 3. Busca os títulos dos cursos usando a classe 'card-header'
    cursos_titulos = driver.find_elements(By.CLASS_NAME, "card-header")
    
    if cursos_titulos:
        print(f"{len(cursos_titulos)} cursos encontrados:")
        for i, card in enumerate(cursos_titulos, 1):
            print(f"  {i}. {card.text.strip()}")
    else:
        print("Nenhum curso encontrado com classe 'card-header'.")

    # 4. Print da tela
    driver.save_screenshot("unifil_presencial_cards.png")
    print("Print salvo como 'unifil_presencial_cards.png'.")

except Exception as e:
    print("Erro durante o teste:", e)

finally:
    time.sleep(2)
    driver.quit()
