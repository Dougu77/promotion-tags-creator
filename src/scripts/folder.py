from models.consts import *
import os

def create_temp_folder() -> None:
    os.makedirs(TEMP_FOLDER)

def delete_temp_folder() -> None:
    os.remove(TEMP_FOLDER)

def create_pdf_folder() -> None:
    os.makedirs(PDF_FOLDER, exist_ok=True)
