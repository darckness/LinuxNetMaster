import customtkinter as ctk
import tkinter as tk
from PIL import Image


def open_new_window():
    import customtkinter as ctk
    import os

    # Configurações iniciais
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    # Janela principal
    root = ctk.CTk()
    root.title("Configuração")
    root.geometry("400x350")

    # Função para carregar as informações do arquivo
    def carregar_informacoes():
        if os.path.exists("configuracoes.txt"):
            with open("configuracoes.txt", "r") as file:
                lines = file.readlines()
                if len(lines) >= 3:
                    entry1.insert(0, lines[0].strip().split(": ")[1])
                    entry2.insert(0, lines[1].strip().split(": ")[1])
                    entry3.insert(0, lines[2].strip().split(": ")[1])

    # Função para salvar as informações em um arquivo
    def salvar_informacoes():
        item1 = entry1.get()
        item2 = entry2.get()
        item3 = entry3.get()

        with open("configuracoes.txt", "w") as file:
            file.write(f"Item 1: {item1}\n")
            file.write(f"Item 2: {item2}\n")
            file.write(f"Item 3: {item3}\n")
        print("Informações salvas com sucesso!")

    # Frame para as entradas
    frame = ctk.CTkFrame(root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Entradas de texto
    label1 = ctk.CTkLabel(frame, text="Item 1:")
    label1.pack(pady=5)
    entry1 = ctk.CTkEntry(frame)
    entry1.pack(pady=5)

    label2 = ctk.CTkLabel(frame, text="Item 2:")
    label2.pack(pady=5)
    entry2 = ctk.CTkEntry(frame)
    entry2.pack(pady=5)

    label3 = ctk.CTkLabel(frame, text="Item 3:")
    label3.pack(pady=5)
    entry3 = ctk.CTkEntry(frame)
    entry3.pack(pady=5)

    # Botão de salvar
    save_button = ctk.CTkButton(frame, text="Salvar", command=salvar_informacoes)
    save_button.pack(pady=20)

    # Carregar informações do arquivo ao iniciar
    carregar_informacoes()

    # Iniciar o loop principal
    root.mainloop()
