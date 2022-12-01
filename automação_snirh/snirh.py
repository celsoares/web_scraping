from playwright.sync_api import sync_playwright
import time


with open("albufeiras.csv", "r", encoding="utf_8") as file:
    barragens=file.readlines()
barragens_split=[]

for x in range(len(barragens)):
    barragens_split.append(barragens[x].split(";"))

print(barragens_split)

with sync_playwright() as p:

    browser=p.chromium.launch(headless=False) #headless --> Mostra o browser enquanto executa
    
    page=browser.new_page()
    
    for x in barragens_split:
    
        page.goto("https://snirh.apambiente.pt/index.php?idMain=1&idItem=1.3")

        #page.fill(local, conteudo)
        #page.locator(local)
        
        page.locator('//*[@id="fs_albufbacia"]').select_option(x[0])
        page.locator('//*[@id="fs_albufalbufeira"]').select_option(x[2])
        page.locator('//*[@id="bolalbuf_utilbts2"]/a[1]').click()
        max_cap=page.locator('//*[@id="bolalbuftbl"]/tbody/tr[1]/td[1]').text_content().strip(" ")
        max_cap=max_cap.replace(" ", "")
        aux=page.locator('//*[@id="bolalbuftbl"]/tbody/tr[3]/td[1]').text_content()
        aux=aux.replace(" ", "")
        aux=aux.split("(")
        current_cap=aux[0]
        x[3]=x[3].strip("\n")
        with open("registo.csv", "a", encoding="utf_8") as file:
            file.write(f"{x[1]};{x[3]};{max_cap};{current_cap}\n")

        print(f"Bacia: {x[1]} --> Alfufeira: {x[3]} ----- Feito")
    #time.sleep(5)
    browser.close()
