from time import sleep
import pyautogui
import pytesseract


def open_calculator():
    pyautogui.press("winleft")
    sleep(0.2)
    pyautogui.write("calculadora", interval=0.1)
    sleep(0.2)
    pyautogui.press("enter")
    sleep(0.2)


def localizar_campo(path: str, confianca: float):
    try:
        elemento = pyautogui.locateCenterOnScreen(path, confidence=confianca, grayscale=True)
        if elemento:
            return elemento
        return None
    except Exception as e:
        print(f"Erro ao localizar o campo: {e}")
        return None
    
def captura_resultado(regiao):
    screenshot = pyautogui.screenshot(region=regiao)
    caminho_screenshot = "captura.png"
    screenshot.save(caminho_screenshot)
    resultado = pytesseract.image_to_string(screenshot, config='--psm 7')
    return resultado.strip()

        

if __name__ == "__main__":
    img_button_1 = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao1.PNG"
    img_button_2 = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao2.PNG"
    img_button_9 = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao9.PNG"
    img_button_plus = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao_plus.PNG"
    img_button_reso = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao_reso.PNG"
    img_button_ce = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao_ce.PNG"
    img_button_close = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao_close.PNG"
    img_testeErro = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\testeErro.PNG"
    img_areaResul = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\area_resultado.PNG"
    img_button_div = "C:\\Users\\vinic\\OneDrive\\Documentos\\Projetos\\MvTest\\images\\botao_div.PNG"

    open_calculator()
    sleep(0.5)


    pos_img_botao_1 = localizar_campo(
        path=img_button_1,
        confianca=0.8
    )
    if pos_img_botao_1:
        pyautogui.mouseUp(pos_img_botao_1)
        sleep(0.2)
        print(pyautogui.position())
        sleep(0.2)
        pyautogui.click(interval=0.5)
        sleep(0.2)
        pyautogui.click(interval=0.5)

    else:
        pyautogui.alert('Botão 1 não encontrado.')


    pos_img_botao_plus = localizar_campo(
        path=img_button_plus,
        confianca=0.8
    )
    if pos_img_botao_plus:
        pyautogui.mouseUp(pos_img_botao_plus)
        sleep(0.2)
        print(pyautogui.position())
        sleep(0.2)
        pyautogui.click(interval=0.5)
    else:
        pyautogui.alert("Botão plus não encontrado.")    


    pos_img_botao_2 = localizar_campo(
        path=img_button_2,
        confianca=0.8
    )
    if pos_img_botao_2:
        pyautogui.mouseUp(pos_img_botao_2)
        sleep(0.2)
        print(pyautogui.position())
        sleep(0.2)
        pyautogui.click(interval=0.5)
    else:
        pyautogui.alert("Botão 2 não encontrado.")


    pos_img_botao_reso = localizar_campo(
        path=img_button_reso,
        confianca=0.8
    )
    if pos_img_botao_reso:
        pyautogui.mouseUp(pos_img_botao_reso)
        sleep(0.2)
        print(pyautogui.position())
        sleep(0.2)
        pyautogui.click(interval=0.5)
    else:
        pyautogui.alert("Botão igual não encontrado.")


    pos_img_botao_div = localizar_campo(
        path=img_button_div,
        confianca=0.8
    )
    if pos_img_botao_div:
        pyautogui.mouseUp(pos_img_botao_div)
        sleep(0.2)
        print(pyautogui.position())
        sleep(0.2)
        pyautogui.click(interval=0.5)
        sleep(0.2)

    else:
        pyautogui.alert('Botão Divisão não encontrado.')


    pos_img_botao_9 = localizar_campo(
        path=img_button_9,
        confianca=0.8
    )
    if pos_img_botao_9:
        pyautogui.mouseUp(pos_img_botao_9)
        sleep(0.2)
        print(pyautogui.position())
        sleep(0.2)
        pyautogui.click(interval=0.5)
    else:
        pyautogui.alert("Botão 9 não encontrado.")


    pyautogui.mouseUp(pos_img_botao_reso)
    sleep(0.2)
    print(pyautogui.position())
    sleep(0.2)
    pyautogui.click(interval=0.5)


    print("tres segundos para tirar a print")
    sleep(3)
            #Print resultado
    pos_area_resultado = localizar_campo(

        path= img_areaResul,
        confianca=0.8
    )
    if pos_area_resultado:
        posicao_x =  int(pos_area_resultado[0]-360)
        posicao_y =  int(pos_area_resultado[1]+ 65)

        region_resultado = (posicao_x, posicao_y, 380, 80)
        resultado = captura_resultado(region_resultado)
        print(f"Resultado da calculadora: {resultado}")
    else:
        print("Área do resultado não encontrada.")


    pos_img_botao_ce = localizar_campo(
        path=img_button_ce,
        confianca=0.8
    )
    if pos_img_botao_ce:
        pyautogui.mouseUp(pos_img_botao_ce)
        sleep(0.2)
        print(pyautogui.position())
        sleep(0.2)
        pyautogui.click(interval=0.5)
    else:
        pyautogui.alert("Botão CE não encontrado.")


    pos_img_botao_close = localizar_campo(
        path=img_button_close,
        confianca=0.8
    )
    if pos_img_botao_close:
        pos_img_botao_close_x = pos_img_botao_close[0] + 2
        pos_img_botao_close_y = pos_img_botao_close[1] - 19
        pyautogui.moveTo(pos_img_botao_close_x, pos_img_botao_close_y)
        pyautogui.mouseUp(pos_img_botao_close_x, pos_img_botao_close_y)
        sleep(0.2)
        pyautogui.click(interval=0.5)
    else:
        pyautogui.alert("Botão Fechar não encontrado")


             #   função encontrar posição
        # print(pos_area_resultado[0], pos_area_resultado[1])
        # sleep(3)
        # mousePosition = pyautogui.position()
        # print(mousePosition)