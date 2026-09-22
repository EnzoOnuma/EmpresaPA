# Dupla: João Pedro Formiga Baptista e Matheus Henriques Geroldo - Turma B 1ºDS
import os

ARQUIVO_PRODUTOS = "produtos.txt"

def executar_produtos():
    def menu():
        print("\n===== MENU DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("0 - Voltar ao menu principal")