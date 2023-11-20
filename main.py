import tkinter as tk
import libs
janelamain = tk.Tk()
janelamain.title("Politec Project")
janelamain.geometry("400x540")

# Botão para abrir a janela de hash
janela_hash_button = tk.Button(janelamain, text="Abrir janela\n de hash", command=libs.abrir_janela_hash)
janela_hash_button.place(x=0, y=0)

# Iniciar a interface gráfica
janelamain.mainloop()
