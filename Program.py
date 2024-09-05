import tkinter as tk
from tkinter import messagebox

# Variáveis globais
nova_operacao = False
historico = []

# Função para atualizar a expressão na entrada de texto
def clicar_botao(valor):
    global nova_operacao
    if nova_operacao:
        entrada.delete(0, tk.END)  # Limpar o visor se for uma nova operação
        nova_operacao = False
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, atual + str(valor))

# Função para calcular o resultado da expressão
def calcular():
    global nova_operacao, historico
    try:
        resultado = eval(entrada.get().replace('X', '*').replace('÷', '/').replace('%', '/100'))
        historico.append(entrada.get() + " = " + str(resultado))  # Armazena no histórico
        if len(historico) > 10:  # Mantém no máximo 10 itens
            historico.pop(0)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
        nova_operacao = True  # Marca que uma nova operação foi feita
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")
        nova_operacao = True

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)

# Função para mostrar o histórico
def mostrar_historico():
    if historico:
        messagebox.showinfo("Histórico", "\n".join(historico))
    else:
        messagebox.showinfo("Histórico", "Nenhuma operação realizada ainda.")

# Função para adicionar porcentagem
def adicionar_porcentagem():
    valor = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, valor + "%")

# Função para adicionar parênteses
def adicionar_parenteses():
    valor = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, valor + "()")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Criando o campo de entrada (visor) para ocupar toda a largura
entrada = tk.Entry(janela, width=30, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
entrada.grid(row=0, column=0, columnspan=4, pady=10)

# Criando os botões de números e operações com a nova organização
botoes = [
    ('C', 1, 0, 'red'), ('÷', 1, 1, 'green'), ('X', 1, 2, 'green'), ('-', 1, 3, 'green'),
    ('H', 2, 0, 'black'), ('%', 2, 1, 'black'), ('()', 2, 2, 'black'), ('+', 2, 3, 'green'),
    ('7', 3, 0, 'black'), ('8', 3, 1, 'black'), ('9', 3, 2, 'black'), ('=', 3, 3, 'black'),
    ('4', 4, 0, 'black'), ('5', 4, 1, 'black'), ('6', 4, 2, 'black'), ('0', 4, 3, 'black'),
    ('1', 5, 0, 'black'), ('2', 5, 1, 'black'), ('3', 5, 2, 'black'),
]

# Adicionando os botões à janela
for (texto, linha, coluna, cor) in botoes:
    if texto == '=':
        botao = tk.Button(janela, text=texto, width=10, height=3, font=('Arial', 18), command=calcular,
                          bg=cor, fg='white', relief='flat', bd=5)
    elif texto == 'C':
        botao = tk.Button(janela, text=texto, width=10, height=3, font=('Arial', 18), command=limpar,
                          bg='white', fg=cor, relief='flat', bd=5)
    elif texto == 'H':
        botao = tk.Button(janela, text=texto, width=10, height=3, font=('Arial', 18), command=mostrar_historico,
                          bg=cor, fg='white', relief='flat', bd=5)
    elif texto == '%':
        botao = tk.Button(janela, text=texto, width=10, height=3, font=('Arial', 18), command=adicionar_porcentagem,
                          bg=cor, fg='white', relief='flat', bd=5)
    elif texto == '()':
        botao = tk.Button(janela, text=texto, width=10, height=3, font=('Arial', 18), command=adicionar_parenteses,
                          bg=cor, fg='white', relief='flat', bd=5)
    else:
        botao = tk.Button(janela, text=texto, width=10, height=3, font=('Arial', 18), 
                          command=lambda t=texto: clicar_botao(t), bg=cor, fg='white', relief='flat', bd=5)
    botao.grid(row=linha, column=coluna, padx=5, pady=5)

# Iniciando o loop principal da janela
janela.mainloop()
