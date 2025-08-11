from enum import Enum

class FileData(str, Enum):
    TEMP_FOLDER = 'temp'
    PDF_FOLDER_AND_FORMAT = 'pdf'
    IMAGE_FORMAT = 'png'
