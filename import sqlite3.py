import sqlite3
import os

# Descobre exatamente onde este arquivo .py está salvo no computador
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(diretorio_atual, "sistema.db")

# Conecta ao banco usando o caminho completo e seguro
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

# Cria a tabela caso ela ainda não exista
cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        nome TEXT,
        preco REAL,
        quantidade INTEGER
    )
""")

conexao.commit()

# --- FUNÇÕES DO SISTEMA ---

def cadastrar_produto():
    print("\n--- CADASTRO DE NOVOS PRODUTOS ---")
    while True:
        try:
            nome = input("1. Digite o nome do produto (ou digite 'sair' para voltar): ").strip()
            
            if nome.lower() == 'sair':
                break
                
            if not nome:
                print("O nome não pode estar vazio. Tente novamente.\n")
                continue
                
            preco = float(input("2. Digite o preço (R$) [Ex: 5.00]: "))
            quantidade = int(input("3. Digite a quantidade em estoque [Ex: 10]: "))
            
            cursor.execute("INSERT INTO produtos VALUES (?, ?, ?)", (nome, preco, quantidade))
            conexao.commit()
            
            print(f"-> Sucesso! Produto '{nome}' cadastrado.\n")
            
        except ValueError:
            print("Erro: Digite valores numéricos válidos para preço e quantidade!\n")


def consultar_produtos():
    print("\n--- CONSULTA DE PRODUTOS CADASTRADOS ---")
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    
    if not produtos:
        print("Nenhum produto cadastrado.\n")
    else:
        for produto in produtos:
            print(f"Nome: {produto[0]} | Preço: R$ {produto[1]:.2f} | Quantidade: {produto[2]}")
        print()

# Executar as funções
cadastrar_produto()
consultar_produtos()

# Fechar a conexão
conexao.close()