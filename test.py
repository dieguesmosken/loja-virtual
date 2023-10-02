import tkinter as tk
from tkinter import messagebox

# Função para adicionar um novo produto ao estoque
def adicionar_produto():
    nome_produto = nome_entry.get()
    quantidade_produto = quantidade_entry.get()
    
    if nome_produto and quantidade_produto:
        lista_estoque.insert(tk.END, f"{nome_produto} - {quantidade_produto} unidades")
        nome_entry.delete(0, tk.END)
        quantidade_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos Vazios", "Preencha todos os campos!")

# Função para remover um produto do estoque
def remover_produto():
    selecao = lista_estoque.curselection()
    if selecao:
        lista_estoque.delete(selecao)
    else:
        messagebox.showwarning("Nenhum Produto Selecionado", "Selecione um produto para remover!")

# Criação da janela principal
root = tk.Tk()
root.title("Gerenciamento de Estoque")

# Criação dos widgets
nome_label = tk.Label(root, text="Nome do Produto:")
quantidade_label = tk.Label(root, text="Quantidade:")
nome_entry = tk.Entry(root)
quantidade_entry = tk.Entry(root)
adicionar_button = tk.Button(root, text="Adicionar Produto", command=adicionar_produto)
remover_button = tk.Button(root, text="Remover Produto Selecionado", command=remover_produto)
lista_estoque = tk.Listbox(root)

# Posicionamento dos widgets
nome_label.pack()
nome_entry.pack()
quantidade_label.pack()
quantidade_entry.pack()
adicionar_button.pack()
remover_button.pack()
lista_estoque.pack()

# Loop principal da aplicação
root.mainloop()
