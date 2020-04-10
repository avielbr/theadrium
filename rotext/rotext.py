import keyboard
import pyperclip
from time import sleep
import pyautogui


def converter(text):
    eng_heb = {'a': 'ש', 'b': 'נ', 'c': 'ב', 'd': 'ג', 'e': 'ק', 'f': 'כ', 'g': 'ע',
               'h': 'י', 'i': 'ן', 'j': 'ח', 'k': 'ל', 'l': 'ך', 'm': 'צ', 'n': 'מ',
               'o': 'ם', 'p': 'פ', 'q': '/', 'r': 'ר', 's': 'ד', 't': 'א', 'u': 'ו',
               'v': 'ה', 'w': "'", 'x': 'ס', 'y': 'ט', 'z': 'ז', ",": 'ת'}

    heb_eng = {'ש': 'a', 'נ': 'b', 'ב': 'c', 'ג': 'd', 'ק': 'e', 'כ': 'f', 'ע': 'g',
               'י': 'h', 'ן': 'i', 'ח': 'j', 'ל': 'k', 'ך': 'l', 'צ': 'm', 'מ': 'n',
               'ם': 'o', 'פ': 'p', '/': 'q', 'ר': 'r', 'ד': 's', 'א': 't', 'ו': 'u',
               'ה': 'v', "'": "w", 'ס': 'x', 'ט': 'y', 'ז': 'z', 'ת': ","}
    result = []

    if text[0] in eng_heb:
        for character in text:
            try:
                result.append(eng_heb[character])
            except:
                result.append(character)
    else:
        for character in text:
            try:
                result.append(heb_eng[character])
            except:
                result.append(character)
    return ''.join(result)


def string_handler():
    sleep(0.1)

    pyautogui.hotkey('ctrl', 'a')
    sleep(0.1)

    pyautogui.hotkey('ctrl', 'c')
    sleep(0.1)

    text = list(pyperclip.paste())
    sleep(0.1)

    result = converter(text)
    sleep(0.1)

    pyperclip.copy(result)
    sleep(0.1)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('alt', 'shift')


keyboard.add_hotkey('ctrl+\\', string_handler)
keyboard.wait()
