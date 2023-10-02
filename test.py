import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para adicionar um novo produto ao estoque e salvar no banco de dados
def adicionar_produto():
    nome_produto = nome_entry.get()
    quantidade_produto = quantidade_entry.get()
    
    if nome_produto and quantidade_produto:
        # Atualizar a interface gráfica
        lista_estoque.insert(tk.END, f"{nome_produto} - {quantidade_produto} unidades")
        nome_entry.delete(0, tk.END)
        quantidade_entry.delete(0, tk.END)
        
        # Salvar os dados no banco de dados
        conn = sqlite3.connect('estoque.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO estoque (nome, quantidade) VALUES (?, ?)', (nome_produto, quantidade_produto))
        conn.commit()
        conn.close()
    else:
        messagebox.showwarning("Campos Vazios", "Preencha todos os campos!")

# Função para remover um produto do estoque e do banco de dados
def remover_produto():
    selecao = lista_estoque.curselection()
    if selecao:
        produto_selecionado = lista_estoque.get(selecao)
        nome_produto, _ = produto_selecionado.split(' - ')
        
        # Remover da interface gráfica
        lista_estoque.delete(selecao)
        
        # Remover do banco de dados
        conn = sqlite3.connect('estoque.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM estoque WHERE nome = ?', (nome_produto,))
        conn.commit()
        conn.close()
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
