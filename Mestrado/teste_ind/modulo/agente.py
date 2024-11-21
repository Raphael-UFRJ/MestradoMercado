import random
from .ordem import (
    Ordem,
)  # Certifique-se de que o módulo Ordem está importado corretamente


class Agente:
    def __init__(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo = saldo_inicial
        self.ativos = (
            {}
        )  # Dicionário para armazenar a quantidade de cada ativo que o agente possui

    def tomar_decisao(self, mercado, livro_ordens):
        # Escolher um ativo aleatoriamente do mercado
        ativo = random.choice(list(mercado.ativos.values()))

        # Decidir se vai comprar ou vender (50% de chance para cada)
        acao = random.choice(["compra", "venda"])

        # Definir quantidade e preço aleatórios para a ordem
        quantidade = random.randint(10, 100)  # Quantidade entre 10 e 100 unidades
        preco = ativo.preco_medio + random.uniform(
            -1, 1
        )  # Preço próximo ao preço médio do ativo

        # Criar a ordem de compra ou venda
        ordem = Ordem(
            agente=self, ativo=ativo, quantidade=quantidade, preco=preco, tipo=acao
        )

        # Adicionar a ordem ao livro de ordens
        livro_ordens.adicionar_ordem(ordem)
        print(
            f"{self.nome} enviou uma ordem de {acao.upper()} de {quantidade} de {ativo.nome} a {preco:.2f}"
        )
