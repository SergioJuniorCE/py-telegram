import pyperclip
import pyautogui
import time
from io import BytesIO
import win32clipboard  # pip install pywin32
from PIL import Image
import re
import webbrowser

# Config
pyautogui.PAUSE = 0.2

# Constants
LINK_PNG = 'telegram-yt-link.png'
WINDOW_NAME = 'Grupo de trabajo'


def copy_screenshot():
    image = Image.open('screenshot.png')
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


def open_telegram():
    telegram_logo_location = pyautogui.locateOnScreen(
        'telegram-logo.png', confidence=0.8)
    if telegram_logo_location is None:
        pyautogui.alert("Telegram no encontrado")
        return
    telegramx, telegramy = pyautogui.center(telegram_logo_location)
    pyautogui.click(telegramx, telegramy)


def ocr():
    # telegram on taskbar position
    open_telegram()
    # Pinned telegram chat
    pyautogui.click(300, 150)
    # Pinned message on chat
    pyautogui.click(775, 110)
    time.sleep(0.5)
    for _ in range(5):
        pyautogui.press('pagedown')

    try:
        location = pyautogui.locateOnScreen(LINK_PNG, confidence=0.9)
    except Exception as e:
        print(e)
        pyautogui.alert("Link no encontrado")
        return

    if location is None:
        pyautogui.alert("Link no encontrado")
        return

    buttonx, buttony = pyautogui.center(location)

    pyautogui.click(buttonx, buttony + 20, duration=0.1)

    time.sleep(4)
    # Like video
    pyautogui.click(823, 967)
    time.sleep(1)
    pyautogui.screenshot('screenshot.png', region=(
        0, 100, 1400, 900))
    time.sleep(1)
    # Remove like
    pyautogui.click(823, 967)
    # Close window
    pyautogui.hotkey('ctrl', 'w')
    open_telegram()
    pyautogui.click(200, 200, duration=0.1)

    copy_screenshot()
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')


def locate_in_screen(filename, confidence=0.9):
    try:
        location = pyautogui.locateOnScreen(filename, confidence=confidence)
        if location is None:
            pyautogui.alert(f"{filename} no encontrado")
            return None
        buttonx, buttony = pyautogui.center(location)
        return buttonx, buttony
    except Exception as e:
        pyautogui.alert(f"{filename} no encontrado")
        return None

def text_analysis():
    # telegram on taskbar position
    open_telegram()
    # Pinned telegram chat
    pyautogui.click(300, 150)
    # Pinned message on chat
    pyautogui.click(775, 110)
    time.sleep(0.5)
    for i in range(5):
        pyautogui.press('pagedown')
    buttonx, buttony = locate_in_screen('trompetas.png', confidence=0.95)
    buttonx -= 400
    pyautogui.move(buttonx, buttony)
    pyautogui.rightClick()
    pyautogui.moveRel(10, 30)
    pyautogui.click()
    message_text = pyperclip.paste()
    
    mision_numero = re.search(r"Misión (\d+)", message_text)
    if mision_numero:
        numero = mision_numero.group(1)
        print("Número de la misión:", numero)
    
    enlace_youtube = re.search(r"(https?://(?:www\.)?youtube\.com/watch\?v=[A-Za-z0-9_-]+)", message_text)
    if enlace_youtube:
        link = enlace_youtube.group(1)
        print("Enlace de YouTube:", link)
        
    webbrowser.open(link)
    
    time.sleep(4)
    # Like video
    pyautogui.click(823, 967)
    time.sleep(1)
    pyautogui.screenshot('screenshot.png', region=(
        0, 100, 1400, 900))
    time.sleep(1)
    # Remove like
    pyautogui.click(823, 967)
    # Close window
    pyautogui.hotkey('ctrl', 'w')
    open_telegram()
    pyautogui.click(200, 200, duration=0.1)

    copy_screenshot()
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.write(f"Mision {numero} completada")
    # pyautogui.press('enter')
    
    # Buscar la cantidad de minutos en el texto
    patron = r"Tiempo de tarea (\d+) minutos"
    coincidencia = re.search(patron, message_text)

    if coincidencia:
        minutos = int(coincidencia.group(1))
        segundos = minutos * 60
        print(segundos)
        segundos_restantes = 0
        for _ in range(segundos):            
            time.sleep(1)
            segundos_restantes += 1
            # Print tiempo restante en minutos y segundos
            print(f"Tiempo restante: {minutos - (segundos_restantes // 60)} minutos y {(segundos - segundos_restantes) % 60} segundos")
        text_analysis()


if __name__ == '__main__':
    text_analysis()
