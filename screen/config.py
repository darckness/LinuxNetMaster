import customtkinter as ctk
import tkinter as tk
from PIL import Image


def open_new_window():
    """Função para abrir uma nova janela"""
    new_window = ctk.CTk()  # Cria a nova janela
    new_window.title("Configuração")
    new_window.geometry("400x300")  # Define o tamanho da nova janela

    # Adiciona alguns widgets à nova janela
    label = ctk.CTkLabel(new_window, text="Bem-vindo à nova tela!", font=("Arial", 16))
    label.pack(pady=20)

    button = ctk.CTkButton(new_window, text="Fechar", command=new_window.destroy)
    button.pack(pady=10)

    # Exibe a nova janela
    new_window.mainloop()
