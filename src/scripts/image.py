from PIL import Image, ImageDraw
from models.label import Label
from models.consts import *
from textwrap import wrap
from .format import *

def create_label(product:str, price:float) -> Label:
    '''summary_ Gera a etiqueta de promoção

    Args:
        product (str): Nome do produto
        price (float): Preço do produto

    Returns:
        Label: Informações da etiqueta (Produto, Preço, Imagem)
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
    lines = wrap(product, MAX_PRODUCT_CHARACTERS)
    y = PROMOTION_HEIGHT + 20

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=PRODUCT_FONT)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (LABEL_SIZE_PX[0] - text_width) / 2
        draw.text((x, y), line, font=PRODUCT_FONT, fill='black')
        y += text_height + 40
    
    # Preço
    bbox = draw.textbbox((0, 0), format_price(price), PRICE_FONT)
    x = (LABEL_SIZE_PX[0] - (bbox[2] - bbox[0])) / 2
    y = LABEL_SIZE_PX[1] - (bbox[3] - bbox[1]) - 80
    draw.text((x, y), format_price(price), font=PRICE_FONT, fill='black')

    # Retorno
    return Label(product, price, image, format_image_file_name())

def save_all_images(labels:list[Label]) -> None:
    for label in labels:
        label.image.save(label.path)
