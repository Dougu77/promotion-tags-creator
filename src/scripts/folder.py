from models.enums import FileData
import os

def create_temp_folder() -> None:
    '''summary_ Cria a pasta temporária das imagens
    '''

    os.makedirs(FileData.TEMP_FOLDER)

def delete_temp_folder() -> None:
    '''summary_ Apaga a pasta temporária das imagens
    '''

    os.remove(FileData.TEMP_FOLDER)

def create_pdf_folder() -> None:
    '''summary_ Cria a pasta dos pdfs
    '''

    os.makedirs(FileData.PDF_FOLDER_AND_FORMAT, exist_ok=True)
