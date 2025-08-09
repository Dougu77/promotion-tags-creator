from scripts import image, pdf
from models.label import Label


labels: list[Label] = []
for c in range(20):
    labels.append(image.create_label('Teste Teste Teste Teste Teste', 10.5))
image.save_all_images(labels)
pdf.create_pdf(labels)
