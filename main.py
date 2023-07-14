import pyautogui as pg
import webbrowser
import time

command = pg.prompt("Добро пожаловать, введите то что хотите сделать. Для ознакомления с командами - откройте readme.rtf", "Without")

if(command == "Информация" or command == "Information" or command == "Инфа" or command == "info"):
    pg.alert("Without, версия 0.9-Beta, сборка 2307. Создатель программы - Кирилл Дятлов (vk.com/mrkoresh4 или vk.com/kdyatlov99). Обновление от 14 июля 2023. Программа создана с использованием библиотеки PyAutoGUI.", "Without", button="Выход")
    pass

elif(command == "Поиск" or command == "Search" or command == "search" or command == "поиск"):
    req = pg.prompt("Что вы именно хотите найти?", "Without")
    webbrowser.open('google.com')
    time.sleep(2)
    pg.moveTo(887, 468, 0.3)
    pg.click(887, 468)
    pg.typewrite(req)
    pg.typewrite(["enter"])
    pass

if(command == "Скриншот" or command == "Screenshot" or command == "screenshot" or command == "скриншот" or command == "Скрин" or command == "скрин"):
    pg.screenshot("screenshot.png")
    pass

elif(command == "Открыть URL" or command == "открыть URL" or command == "Open URL" or command == "open URL"):
    web = pg.prompt("Какой сайт вы хотите открыть?", "Without")
    webbrowser.open(web)
    pass

elif(command == "Найти видео" or command == "найти видео" or command == "Search video" or command == "search video"):
    video = pg.prompt("Какое видео вы хотите найти?", "Without")
    webbrowser.open("youtube.com")
    pg.moveTo(894, 120, 0.5)
    pg.click(894, 120)
    pg.typewrite(video)
    pg.typewrite(["enter"])
    pass

elif(command == "Создать папку" or command == "Create folder" or command == "создать папку" or command == "create folder"):
    pg.moveTo(1662, 273, 0.5)
    pg.rightClick(1662, 273)
    pg.moveTo(1600, 615, 0.5)
    pg.moveTo(1289, 615, 0.5)
    pg.click(1289, 615)
    pass

elif(command == "Версия Windows" or command == "Windows version" or command == "версия windows" or command == "windows version" or command == "Version Windows" or command == "version windows"):
    pg.moveTo(243, 1056, 0.5)
    pg.click(243, 1056)
    pg.typewrite("cmd")
    pg.moveTo(293, 425, 0.5)
    pg.click(293, 425)
    pg.moveTo(482, 274, 0.5)
    pg.typewrite("winver")
    pg.typewrite(["enter"])
    pass

elif(command == "Открой коммандную строку" or command == "Открой CMD" or command == "Открой cmd" or command == "открой коммандную строку" or command == "открой CMD" or command == "открой cmd" or command == "Open CMD" or command == "open CMD" or command == "open cmd" or command == "Open cmd"):
    pg.moveTo(243, 1056, 0.5)
    pg.click(243, 1056)
    pg.typewrite("cmd")
    pg.moveTo(293, 425, 0.5)
    pg.click(293, 425)
    pass

elif(command == "Открой Пуск" or command == "Открыть Пуск" or command == "Пуск" or command == "открой пуск" or command == "открыть пуск" or command == "пуск" or command == "Open Start" or command == "open start" or command == "start" or command == "Start"):
    pg.hotkey("winleft")
    pass

elif(command == "Исходник" or command == "исходник" or command == "Source" or command == "source" or command == "src"):
    webbrowser.open("https://github.com/KoreshStudio/Without")
    pass

elif(command == "Обновление" or command == "Обновиться" or command == "обновление" or command == "обновиться" or command == "Update"):
    webbrowser.open("https://vk.com/topic-221592680_49822378")
    pass

elif(command == "Выход" or command == "Quit" or command == "quit" or command == "выход"):
    pg.alert("До свидания!", "Without", button="Выход")
    pass

else:
    pg.alert("Команда не найдена", "Without", button="ОК")
    pass
