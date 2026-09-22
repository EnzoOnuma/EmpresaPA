# Dupla: João Pedro Formiga Baptista e Matheus Henriques Geroldo - Turma B 1ºDS
import os

ARQUIVO_PRODUTOS = "produtos.txt"

def executar_produtos():
    def menu():
        print("\n===== MENU DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("0 - Voltar ao menu principal")

    def carregar_produtos():
        produtos = []

        if not os.path.exists(ARQUIVO_PRODUTOS):
            return produtos

        with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as arquivo:
            linhas_brutas = arquivo.readlines()

        for linha_bruta in linhas_brutas:
            linha = linha_bruta.strip()
            try:
                nome, preco = linha.split(";")
                produtos.append((nome, float(preco)))
            except ValueError:
                print(f"Linha inválida ignorada: {linha}")

        return produtos

    def produto_existe(nome):
        produtos = carregar_produtos()
        for nome_cadastrado, preco in produtos:
            if nome_cadastrado.lower() == nome.lower():
                return True
        return False