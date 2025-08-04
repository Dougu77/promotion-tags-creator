#  # Cria PDF
#     pdf = FPDF(orientation='P', unit='mm', format='A4')
#     pdf.set_auto_page_break(0)
#     pdf.add_page()

#     # Espaçamento entre etiquetas
#     margem_lateral = 10
#     margem_superior = 10
#     espacamento_h = 5
#     espacamento_v = 5

#     x = margem_lateral
#     y = margem_superior

#     for idx, path in enumerate(etiquetas):
#         pdf.image(path, x=x, y=y, w=LABEL_WIDTH_MM, h=LABEL_HEIGHT_MM)
#         os.remove(path)

#         x += LABEL_WIDTH_MM + espacamento_h

#         # Se passar da largura da página, quebra linha
#         if x + LABEL_WIDTH_MM > 210 - margem_lateral:
#             x = margem_lateral
#             y += LABEL_HEIGHT_MM + espacamento_v
#             # Se passar da altura da página, nova página
#             if y + LABEL_HEIGHT_MM > 297 - margem_superior:
#                 pdf.add_page()
#                 x = margem_lateral
#                 y = margem_superior

#     output = "etiquetas_promocao.pdf"
#     pdf.output(output)
#     print(f"PDF '{output}' criado com sucesso!")
