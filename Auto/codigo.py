# entrar no sistema
# login
# abrir a base de dados
# cadastrar o produto
# repetir

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=405, y=380)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua_senha")
pyautogui.press("enter")
time.sleep(3)

prod = pandas.read_csv("produtos.csv").to_dict("records")

for p in prod:
    pyautogui.click(x=357, y=293)
    pyautogui.write(str(p["codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(p["marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(p["tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(p["categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(p["preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(p["custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(p["obs"]))
    pyautogui.press("enter")
    pyautogui.scroll(5000)