from PIL import ImageFont

LABEL_SIZE_MM = (100, 70)
LABEL_SIZE_PX = (1181, 827)

A4_SIZE_MM = (210, 297)
A4_SIZE_PX = (2480, 3508)

PRODUCT_FONT = ImageFont.truetype('arial.ttf', 90)
PRICE_FONT = ImageFont.truetype('arial.ttf', 140)

PROMOTION_COLOR = 'red'
PROMOTION_TEXT = 'PROMOÇÃO'
PROMOTION_FONT = ImageFont.truetype('arial.ttf', 90)
PROMOTION_HEIGHT = LABEL_SIZE_PX[1] * 0.25

TEMP_FOLDER = 'temp'
