1  # BLOCO A: A Interface da Barreira
2  janela_login = ctk.CTk()
3  janela_login.geometry("300x350")
4  entry_user = ctk.CTkEntry(janela_login, placeholder_text="Usuário")
5  entry_user.pack(pady=10)
6  # NOVO: Oculta o texto digitado na tela
7  entry_senha = ctk.CTkEntry(janela_login, placeholder_text="Senha", show="*")
8  entry_senha.pack(pady=10)
9  ctk.CTkButton(janela_login, text="Autenticar", command=validar_login).pack(pady=30)
10 janela_login.mainloop()
11 
12 # -------------------------------------------------------------
13 # BLOCO B: O Encapsulamento do Sistema Base
14 def abrir_sistema_principal():
15     # NOVO: Encerra e destrói a janela de login atual da memória
16     janela_login.destroy()
17     # NOVO: Permite que outras funções enxerguem a lista de produtos
18     global frame_lista
19 
20     # === AQUI ENTRA TODO O CÓDIGO DA JANELA PRINCIPAL QUE VOCÊS JÁ FIZERAM ===
21     janela = ctk.CTk()
22     janela.mainloop()
23 
24 # -------------------------------------------------------------
25 # BLOCO C: A Função de Validação

def validar_login():
    if entry_user.get() == "admin" and entry_senha.get() == "123":
        abrir_sistema_principal()  # Libera a inicialização do sistema
    else:
        messagebox.showerror("Acesso negado", "Credenciais inválidas")