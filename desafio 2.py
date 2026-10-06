def realizar_venda(nome_produto):
    # 1. Consulta no banco de dados
    cursor.execute(
        "SELECT quantidade FROM produtos WHERE nome = ?", (nome_produto,)
    )  #[cite: 38]
    resultado = cursor.fetchone()  #[cite: 38]

    if resultado:
        gtd_atual = resultado[0]  #[cite: 38]

        # 2. Regra de Negócio: Impede saldo negativo
        if gtd_atual > 0:  #[cite: 30, 38]
            nova_qtd = gtd_atual - 1  # Processamento da baixa na RAM[cite: 30, 38]
            cursor.execute(
                "UPDATE produtos SET quantidade = ? WHERE nome = ?",
                (nova_qtd, nome_produto),
            )  #[cite: 30, 38]
            conexao.commit()  # Confirmação da gravação no banco[cite: 38]
            atualizar_lista_produtos()  # Atualiza a interface[cite: 38]
        else:  # Tratamento da exceção de saldo zero[cite: 38]
            messagebox.showwarning(
                "Aviso", "Produto Esgotado!"
            )  #[cite: 30, 38]