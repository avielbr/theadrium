import keyboard
import pyperclip
from time import sleep
import pyautogui
import string
from googletrans import Translator


class Maps:
    en_iw = {'a': 'ש', 'b': 'נ', 'c': 'ב', 'd': 'ג', 'e': 'ק', 'f': 'כ', 'g': 'ע',
             'h': 'י', 'i': 'ן', 'j': 'ח', 'k': 'ל', 'l': 'ך', 'm': 'צ', 'n': 'מ',
             'o': 'ם', 'p': 'פ', 'q': '/', 'r': 'ר', 's': 'ד', 't': 'א', 'u': 'ו',
             'v': 'ה', 'w': "'", 'x': 'ס', 'y': 'ט', 'z': 'ז', '.': 'ץ', ",": 'ת'}

    iw_en = {'ש': 'a', 'נ': 'b', 'ב': 'c', 'ג': 'd', 'ק': 'e', 'כ': 'f', 'ע': 'g',
             'י': 'h', 'ן': 'i', 'ח': 'j', 'ל': 'k', 'ך': 'l', 'צ': 'm', 'מ': 'n',
             'ם': 'o', 'פ': 'p', '/': 'q', 'ר': 'r', 'ד': 's', 'א': 't', 'ו': 'u',
             'ה': 'v', "'": "w", 'ס': 'x', 'ט': 'y', 'ז': 'z', 'ת': ",", 'ץ': "."}


# Translates selected text.
# First copies and pastes text into a variable, then recognizes source language and
# translates accordingly.
def translate():
    trans = Translator()

    pyautogui.hotkey('ctrl', 'c')
    sleep(0.1)
    text = pyperclip.paste()

    if text[0] in Maps.iw_en:
        result = trans.translate(text)
        pyperclip.copy(result.text)

    elif text[0].lower() in Maps.en_iw:
        result = trans.translate(text, dest='iw')
        pyperclip.copy(result.text)

    pyautogui.hotkey('ctrl', 'v')


def converter(text):
    # Initializing list
    result = []

    # Initializing index of first character in text
    first_char = 0

    # This accounts for the situation in which the string starts with a punctuation mark.
    # If the rec'd text is just a single punctuation mark, it will remain the same, unless
    # it is a comma, which maps to ת.
    if len(text) > 1:
        while text[first_char] in string.punctuation:
            first_char += 1

    if text[first_char] in Maps.en_iw:
        for character in text:
            try:
                result.append(Maps.en_iw[character])
            except LookupError:
                result.append(character)
    else:
        for character in text:
            try:
                result.append(Maps.iw_en[character])
            except LookupError:
                result.append(character)
    return ''.join(result)


def string_handler():
    pyautogui.hotkey('ctrl', 'a')

    pyautogui.hotkey('ctrl', 'c')
    sleep(0.1)

    text = list(pyperclip.paste())

    result = converter(text)
    sleep(0.1)

    pyperclip.copy(result)
    sleep(0.1)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('alt', 'shift')


# Hotkey for flipping text according to maps
keyboard.add_hotkey('ctrl+\\', string_handler)

# Hotkey for translating selected text
keyboard.add_hotkey('ctrl+]', translate)
keyboard.wait()
