import os
import sqlite3
from tkinter import messagebox
import customtkinter as ctk

# Caminho seguro para o banco de dados
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(diretorio_atual, "sistema.db")


# Função para conectar ao banco de dados e criar a tabela
def conectar():
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS produtos (
            nome TEXT PRIMARY KEY,
            preco REAL,
            quantidade INTEGER
        )
    """
    )
    conexao.commit()
    return conexao, cursor


# ==========================================
# REGRAS DE NEGÓCIO E OPERAÇÕES DO SISTEMA
# ==========================================


def cadastrar_produto():
    nome = entry_nome.get().strip()
    preco_str = entry_preco.get().strip()
    quantidade_str = entry_quantidade.get().strip()

    if not nome:
        messagebox.showwarning("Aviso", "O nome não pode estar vazio!")
        return

    try:
        preco = float(preco_str)
        quantidade = int(quantidade_str)
    except ValueError:
        messagebox.showerror(
            "Erro de Digitação", "Digite valores numéricos válidos!"
        )
        return

    # Bloqueia valores negativos
    if preco < 0 or quantidade < 0:
        messagebox.showwarning("Aviso", "Valores não podem ser negativos!")
        return

    conexao, cursor = conectar()

    # Checagem de Duplicidade
    cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome,))
    if cursor.fetchone():
        messagebox.showwarning("Aviso", "Este produto já está cadastrado!")
        entry_nome.delete(0, "end")
        conexao.close()
        return

    cursor.execute(
        "INSERT INTO produtos VALUES (?, ?, ?)", (nome, preco, quantidade)
    )
    conexao.commit()
    conexao.close()

    messagebox.showinfo("Sucesso", f"Produto '{nome}' cadastrado!")

    entry_nome.delete(0, "end")
    entry_preco.delete(0, "end")
    entry_quantidade.delete(0, "end")


def consultar_produtos():
    conexao, cursor = conectar()
    cursor.execute("SELECT * FROM produtos")
    itens = cursor.fetchall()
    conexao.close()

    caixa_resultados.configure(state="normal")
    caixa_resultados.delete("1.0", "end")

    if not itens:
        caixa_resultados.insert(
            "end", "Nenhum produto cadastrado no banco de dados.\n"
        )
    else:
        for linha in itens:
            texto = f"Produto: {linha[0]:<15} | Preço: R$ {linha[1]:>6.2f} | Estoque: {linha[2]}\n"
            caixa_resultados.insert("end", texto)

    caixa_resultados.configure(state="disabled")


# ==========================================
# BLOCO B: O Encapsulamento do Sistema Base
# ==========================================
def abrir_sistema_principal():
    # NOVO: Encerra e destrói a janela de login atual da memória
    janela_login.destroy()  #

    # Variáveis globais para os componentes da janela principal
    global entry_nome, entry_preco, entry_quantidade, caixa_resultados

    # === AQUI ENTRA O CÓDIGO DA JANELA PRINCIPAL ===[cite: 32, 33, 34]
    janela = ctk.CTk()
    janela.title("Lanchonete Ennius Muniz - Senac-DF")
    janela.geometry("500x600")

    # Componentes da Interface de Cadastro
    lbl_nome = ctk.CTkLabel(janela, text="Nome do Produto:")
    lbl_nome.pack(pady=(10, 0))
    entry_nome = ctk.CTkEntry(janela, width=300)
    entry_nome.pack(pady=5)

    lbl_preco = ctk.CTkLabel(janela, text="Preço (R$):")
    lbl_preco.pack(pady=(10, 0))
    entry_preco = ctk.CTkEntry(janela, width=300)
    entry_preco.pack(pady=5)

    lbl_quantidade = ctk.CTkLabel(janela, text="Quantidade:")
    lbl_quantidade.pack(pady=(10, 0))
    entry_quantidade = ctk.CTkEntry(janela, width=300)
    entry_quantidade.pack(pady=5)

    btn_salvar = ctk.CTkButton(
        janela,
        text="Salvar Produto",
        fg_color="green",
        command=cadastrar_produto,
    )
    btn_salvar.pack(pady=15)

    btn_consultar = ctk.CTkButton(
        janela, text="Consultar Produtos Salvos", command=consultar_produtos
    )
    btn_consultar.pack(pady=10)

    caixa_resultados = ctk.CTkTextbox(janela, width=420, height=180)
    caixa_resultados.pack(pady=10)
    caixa_resultados.configure(state="disabled")

    janela.mainloop()  #[cite: 32, 33, 34]


# ==========================================
# BLOCO C: A Função de Validação
# ==========================================
def validar_login():  #[cite: 32, 33, 34]
    if (
        entry_user.get() == "admin" and entry_senha.get() == "123"
    ):  #[cite: 32, 33, 34]
        abrir_sistema_principal()  # Libera a inicialização do sistema[cite: 32, 33, 34]
    else:
        messagebox.showerror(
            "Acesso negado", "Credenciais inválidas."
        )  #[cite: 32, 33, 34]


# ==========================================
# BLOCO A: A Interface da Barreira (Login)
# ==========================================
janela_login = ctk.CTk()  #[cite: 32, 33, 34]
janela_login.title("Login - Sistema de Segurança")
janela_login.geometry("300x350")  #[cite: 32, 33, 34]

entry_user = ctk.CTkEntry(
    janela_login, placeholder_text="Usuário"
)  #[cite: 32, 33, 34]
entry_user.pack(pady=10)  #[cite: 32, 33, 34]

# NOVO: Oculta o texto digitado na tela (Mascara visual)
entry_senha = ctk.CTkEntry(
    janela_login, placeholder_text="Senha", show="*"
)  #[cite: 31, 32, 33, 34]
entry_senha.pack(pady=10)  #[cite: 32, 33, 34]

btn_autenticar = ctk.CTkButton(
    janela_login, text="Autenticar", command=validar_login
)  #[cite: 32, 33, 34]
btn_autenticar.pack(pady=30)  #[cite: 32, 33, 34]

janela_login.mainloop()  #[cite: 32, 33, 34]