from dataclasses import dataclass
from PIL.Image import Image

@dataclass
class Label:
    product: str
    price: float
    image: Image
    path: str
