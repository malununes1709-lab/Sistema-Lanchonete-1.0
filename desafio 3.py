def atualizar_lista_produtos():
    # Limpa os componentes antigos do frame da lista
    for widget in frame_lista.winfo_children():
        widget.destroy()

    conexao, cursor = conectar()
    cursor.execute("SELECT nome, preco, quantidade FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()

    for produto in produtos:
        nome, preco, qtd = produto

        # 1. Passo 01 e 02: Obter quantidade e definir cor do alerta
        if qtd <= 5:  #[cite: 36, 37]
            cor_alert = "#FF4D4D"  # Vermelho para alerta de estoque baixo[cite: 36, 37]
        else:
            cor_alert = "#22C55E"  # Verde para estoque normal[cite: 37]

        # 3. Passo 03: Criar CTkLabel aplicando text_color=cor_alert
        texto = f"{nome} | R$ {preco:.2f} | Qtd: {qtd}"
        label = ctk.CTkLabel(
            frame_lista,
            text=texto,
            text_color=cor_alert,
            font=("inter", 16),
        )  #[cite: 36, 37]
        label.pack(padx=10, pady=6, anchor="w")  #[cite: 36]