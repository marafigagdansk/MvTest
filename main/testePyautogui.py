from time import sleep
import pyautogui

def open_calculator():
    pyautogui.press("winleft")
    sleep(0.3)
    pyautogui.write("calculadora", interval=0.1)
    sleep(0.3)
    pyautogui.press("enter")
    sleep(0.3)

def localizar_campo(path: str, confianca: float):
    try:
        elemento = pyautogui.locateCenterOnScreen(path, confidence=confianca, grayscale=True)
        if elemento:
            return elemento
        return None
    except Exception as e:
        print(f"Erro ao localizar o campo: {e}")
        return None

if __name__ == "__main__":
    img_button_1 = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao1.PNG"
    img_button_2 = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao2.PNG"
    img_button_min = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao_min.PNG"
    img_button_plus = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao_plus.PNG"
    img_button_reso = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao_reso.PNG"
    img_button_ce = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao_ce.PNG"
    img_button_close = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao_close.PNG"

    pos_img_botao_min = localizar_campo(
        path=img_button_min,
        confianca=0.8
    )
    if pos_img_botao_min:
        pyautogui.mouseUp(pos_img_botao_min)
        sleep(0.3)
        print(pyautogui.position())
        sleep(0.3)
        pyautogui.click(interval=1)
    else:
        print("Botão de minimizar não encontrado.")

    open_calculator()
    sleep(0.5)

    pos_img_botao_1 = localizar_campo(
        path=img_button_1,
        confianca=0.8
    )
    if pos_img_botao_1:
        pyautogui.mouseUp(pos_img_botao_1)
        sleep(0.3)
        print(pyautogui.position())
        sleep(0.5)
        pyautogui.click(interval=1)
        sleep(0.3)
        pyautogui.click(interval=1)
    else:
        print("Botão 1 não encontrado.")

    pos_img_botao_plus = localizar_campo(
        path=img_button_plus,
        confianca=0.8
    )
    if pos_img_botao_plus:
        pyautogui.mouseUp(pos_img_botao_plus)
        sleep(0.3)
        print(pyautogui.position())
        sleep(0.3)
        pyautogui.click(interval=1)
    else:
        print("Botão plus não encontrado.")    

    pos_img_botao_2 = localizar_campo(
        path=img_button_2,
        confianca=0.8
    )
    if pos_img_botao_2:
        pyautogui.mouseUp(pos_img_botao_2)
        sleep(0.3)
        print(pyautogui.position())
        sleep(0.3)
        pyautogui.click(interval=1)
    else:
        print("Botão 2 não encontrado.")

    pos_img_botao_reso = localizar_campo(
        path=img_button_reso,
        confianca=0.8
    )
    if pos_img_botao_reso:
        pyautogui.mouseUp(pos_img_botao_reso)
        sleep(0.3)
        print(pyautogui.position())
        sleep(0.3)
        pyautogui.click(interval=1)
    else:
        print("Botão igual não encontrado.")

    pos_img_botao_ce = localizar_campo(
        path=img_button_ce,
        confianca=0.8
    )
    if pos_img_botao_ce:
        pyautogui.mouseUp(pos_img_botao_ce)
        sleep(0.3)
        print(pyautogui.position())
        sleep(0.3)
        pyautogui.click(interval=1)
    else:
        print("Botão CE não encontrado.")
    
    pos_img_botao_close = localizar_campo(
        path=img_button_close,
        confianca=0.8
    )
    if pos_img_botao_close:
        pos_img_botao_close_x = pos_img_botao_close[0] + 2
        pos_img_botao_close_y = pos_img_botao_close[1] - 19
        pyautogui.moveTo(pos_img_botao_close_x, pos_img_botao_close_y)
        pyautogui.mouseUp(pos_img_botao_close_x, pos_img_botao_close_y)
        sleep(0.3)
        pyautogui.click(interval=1)
    else:
        print("Botão Fechar não encontrado")


            # função encontrar posição
    # print(pos_img_botao_close[0], pos_img_botao_close[1])
    # sleep(3)
    # mousePosition = pyautogui.position()
    # print(mousePosition)