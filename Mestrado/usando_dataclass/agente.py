from dataclasses import dataclass
from typing import List
import random
from usando_dataclass.mercado import Mercado
from usando_dataclass.ordem import Ordem
import numpy as np


@dataclass
class Agente:
    nome: str
    ativo: str
    sentimento: str  # Pode ser "positivo", "negativo" ou "neutro"
    expectativa: List[float]  # [preço mínimo, preço esperado, preço máximo]
    preco: float  # Preço atual que o agente está disposto a negociar
    quantidade: int  # Quantidade de ativos
    conhecimento: str  # "alto", "médio", "baixo"

    def analisar_mercado(self, mercado: Mercado) -> None:
        """Avalia o mercado e ajusta expectativas e ações baseado no sentimento e conhecimento."""
        print(f"{self.nome} analisando o mercado para o ativo {self.ativo}...")
        media_preco = np.mean(
            list(mercado.ativos.values())
        )  # Usar Mercado para obter ativos
        desvio_padrao = np.std(list(mercado.ativos.values()))
        print(
            f"Analisando mercado, preço médio: {media_preco}, desvio padrão: {desvio_padrao}"
        )

        # Ajuste de expectativa com base no sentimento
        if self.sentimento == "positivo":
            self.preco = min(self.expectativa[2], self.preco * 1.05)
        elif self.sentimento == "negativo":
            self.preco = max(self.expectativa[0], self.preco * 0.95)
        else:
            self.preco = self.expectativa[
                1
            ]  # Sentimento neutro, segue o preço esperado

        # Ajuste baseado no conhecimento
        if self.conhecimento == "alto":
            self.preco += random.uniform(-0.5, 0.5)
        elif self.conhecimento == "baixo":
            self.preco += random.uniform(-1.0, 1.0)

    def tomar_decisao(self, mercado: Mercado, order_book) -> None:
        """Toma uma decisão de compra ou venda para o ativo específico após análise."""
        self.analisar_mercado(mercado)  # Passar o Mercado para a análise

        # Decisão de compra ou venda
        if random.random() > 0.5:
            print(
                f"{self.nome} decidiu comprar {self.quantidade} de {self.ativo} a {self.preco}"
            )
            order_book.adicionar_ordem(
                Ordem(
                    tipo_ordem="compra",
                    ativo=self.ativo,
                    preco_limite=self.preco,
                    quantidade=self.quantidade,
                )
            )
        else:
            print(
                f"{self.nome} decidiu vender {self.quantidade} de {self.ativo} a {self.preco}"
            )
            order_book.adicionar_ordem(
                Ordem(
                    tipo_ordem="venda",
                    ativo=self.ativo,
                    preco_limite=self.preco,
                    quantidade=self.quantidade,
                )
            )
