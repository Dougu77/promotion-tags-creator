from .consts import *
import os

def format_price(price:float) -> str:
    return f'R$ {price:6.2f}'.replace('.', ',')

def format_image_file_name() -> str:
    files = os.listdir(TEMP_FOLDER)
    return f'{TEMP_FOLDER}/etiqueta_{len(files) + 1}.png'
