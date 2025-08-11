from models.label import Label
from models.consts import *
from fpdf import FPDF
from . import format

def create_pdf(labels:list[Label]) -> None:

    # Criação do PDF
    pdf = FPDF()
    pdf.set_auto_page_break(0)
    pdf.add_page()

    # Definição dos posicionamentos
    gap = 3
    x = gap
    y = gap

    for label in labels:
        pdf.image(label.path, x=x, y=y, w=LABEL_SIZE_MM[0], h=LABEL_SIZE_MM[1])
        x += LABEL_SIZE_MM[0] + gap

        # Verificação para quebra de linha
        if x + LABEL_SIZE_MM[0] > 210 - gap:
            x = gap
            y += LABEL_SIZE_MM[1] + gap

            # Verificação para criação de mais uma página
            if y + LABEL_SIZE_MM[1] > 297 - gap:
                pdf.add_page()
                x = gap
                y = gap

    pdf.output(format.pdf_file_name())
