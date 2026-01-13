import pyautogui
import time
import pandas

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
    
pyautogui.click(x=768, y=358)
pyautogui.write("teste2393@gmail.com")

pyautogui.press("tab")
pyautogui.write("senhaço123")

pyautogui.press("tab")
pyautogui.press("enter")

tabela = pandas.read_csv("material/produtos.csv")

for linha in tabela.index:
    
    pyautogui.click(x=946, y=240)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    

time.sleep(2)