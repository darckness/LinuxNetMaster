import customtkinter as ctk
import tkinter as tk
from PIL import Image

# Configurações iniciais
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Janela principal
root = ctk.CTk()
root.title("LinuxNetMaster")
root.geometry("1000x700")
root.configure(bg='#b3e9f3')

# Carregar a imagem
image_path = "img/AQlogo.png"
image = ctk.CTkImage(light_image=Image.open(image_path), size=(40, 40))

# Frame superior
top_frame = ctk.CTkFrame(root, fg_color='#00c4ff', corner_radius=0, height=100)
top_frame.pack(side=ctk.TOP, fill='x', expand=False)

# Adicionando elementos na barra superior
img_label = ctk.CTkLabel(top_frame, image=image, text="", text_color='black', font=("Arial", 16, "bold"))
img_label.pack(side=ctk.LEFT, padx=20, pady=10)

software_name_label = ctk.CTkLabel(top_frame, text="Linux Net Master", text_color='white', font=("Tahoma", 20, "bold"))
software_name_label.pack(side=ctk.LEFT, padx=20, pady=10)

# Frame esquerdo para os botões
left_frame = ctk.CTkFrame(root, fg_color='#ffffff', corner_radius=0, width=70)
left_frame.pack(side=ctk.LEFT, fill=ctk.Y, padx=0, pady=0)

# Botões na lateral esquerda
# for i in range(4):
#     button = ctk.CTkButton(left_frame, text="Button", width=100, height=40, fg_color='#00c4ff', text_color='black', hover_color='#00b2e6', corner_radius=8)
#     button.pack(pady=10)

# Frame central para os elementos principais
center_frame = ctk.CTkFrame(root, fg_color='#C0F3FC', corner_radius=0)
center_frame.pack(side=ctk.TOP, pady=0, fill='both', expand=True)


# Adicionando caixas de texto
texts = [
    "IEEE 802.11b/g/n 2.4GHz", "IEEE 802.11b/g/n 2.4GHz", "IEEE 802.11a/g/n/ac 2.4GHz",
    "IEEE 802.11a/b/g/n/ac 2.4GHz", "IEEE 802.11a/b/g/n/ac 5GHz", "IEEE 802.11a/b/g/n/ac/ax 5GHz"
]

row = 0
column = 0
for text in texts:
    if column == 3:  # Ajusta para 2 colunas
        row += 1
        column = 0

    box_frame = ctk.CTkFrame(center_frame, fg_color='#00c4ff', width=230, height=350, corner_radius=15)
    box_frame.grid(row=row, column=column, padx=20, pady=20)

    label = ctk.CTkLabel(box_frame, text=text, fg_color='white', text_color='black', font=("Arial", 12), corner_radius=10, height=40)
    label.pack(fill=ctk.X, pady=15, padx=10)

    column += 1

root.mainloop()
