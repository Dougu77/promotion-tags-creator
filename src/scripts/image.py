from PIL import Image, ImageDraw
from .consts import *
from .format import *

def create_label(product:str, price:float) -> None:
    '''summary_ Gera a etiqueta de promoção

    Args:
        product (str): Nome do produto
        price (float): Preço do produto
    '''

    # Configurações iniciais pro pillow
    image = Image.new('RGB', LABEL_SIZE_PX, 'white')
    draw = ImageDraw.Draw(image)
    
    # Desenhos da imagem
    # Faixa superior vermelha
    draw.rectangle([0, 0, LABEL_SIZE_PX[0], PROMOTION_HEIGHT], fill=PROMOTION_COLOR)
    
    # Borda preta
    draw.rectangle([0, 0, LABEL_SIZE_PX[0] - 1, LABEL_SIZE_PX[1] - 1], outline='black', width=3)
    
    # Textos da imagem
    # Promoção (Faixa superior vermelha)
    bbox = draw.textbbox((0, 0), PROMOTION_TEXT, PROMOTION_FONT)
    x = (LABEL_SIZE_PX[0] - (bbox[2] - bbox[0])) / 2
    y = (PROMOTION_HEIGHT - (bbox[3] - bbox[1])) / 2
    draw.text((x, y), PROMOTION_TEXT, font=PROMOTION_FONT, fill='white')

    # Nome do produto
    bbox = draw.textbbox((0, 0), product, font=PRODUCT_FONT)
    x = (LABEL_SIZE_PX[0] - (bbox[2] - bbox[0])) / 2
    y = PROMOTION_HEIGHT + 20
    draw.text((x, y), product, font=PRODUCT_FONT, fill='black')

    # Preço
    bbox = draw.textbbox((0, 0), format_price(price), PRICE_FONT)
    x = (LABEL_SIZE_PX[0] - (bbox[2] - bbox[0])) / 2
    y = LABEL_SIZE_PX[1] - (bbox[3] - bbox[1]) - 80
    draw.text((x, y), format_price(price), font=PRICE_FONT, fill='black')

    # Salvamento da imagem
    if not os.path.exists(TEMP_FOLDER):
        os.makedirs(TEMP_FOLDER)
    image.save(format_image_file_name())
