from scripts import image, pdf
from models.label import Label
import tkinter as tk
from tkinter import ttk

# Lista das etiquetas
labels: list[Label] = []

# Configurações iniciais da interface gráfica
root = tk.Tk()
root.title('Gerador de Etiquetas')

# Definição do layout inicial
main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.columnconfigure(0, weight=7)  # 70%
main_frame.columnconfigure(1, weight=0)  # Separador
main_frame.columnconfigure(2, weight=3)  # 30%

# Aba dos inputs
list_frame = ttk.Frame(main_frame, padding='10')
list_frame.grid(row=0, column=0, sticky='nsew')

# Separador vertical
separator = ttk.Separator(main_frame, orient='vertical')
separator.grid(row=0, column=1, sticky='ns', padx=5)

# Aba dos botões
buttons_frame = ttk.Frame(main_frame, padding='10')
buttons_frame.grid(row=0, column=2, sticky='ns')

# Lista de etiquetas


# Loop para a interface funcionar
root.mainloop()
