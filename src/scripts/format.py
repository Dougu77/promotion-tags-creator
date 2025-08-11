from models.enums import FileData
import os

def price(price:float) -> str:
    return f'R$ {price:6.2f}'.replace('.', ',')

def format_file_name(folder:FileData, format:FileData) -> str:
    files = os.listdir(folder)
    plural = '' if format == FileData.IMAGE_FORMAT else 's'
    return f'{folder}/etiqueta{plural}_{len(files) + 1}.{format}'

def image_file_name() -> str:
    return format_file_name(FileData.TEMP_FOLDER, FileData.IMAGE_FORMAT)

def pdf_file_name() -> str:
    return format_file_name(FileData.PDF_FOLDER_AND_FORMAT, FileData.PDF_FOLDER_AND_FORMAT)
