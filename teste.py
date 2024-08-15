import customtkinter as ctk

# Configurações iniciais
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Janela principal
root = ctk.CTk()
root.title("Configuração")
root.geometry("400x300")

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

# Iniciar o loop principal
root.mainloop()
