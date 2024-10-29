from dataclasses import dataclass
from typing import List
import random
from usando_class.mercado import Mercado


@dataclass
class Agente:
    nome: str
    ativo: str
    sentimento: str  # Pode ser "positivo", "negativo" ou "neutro"
    expectativa: List[
        float
    ]  # Expectativa de preço futuro (ex.: [preço mínimo, preço esperado, preço máximo])
    preco: float  # Preço atual que o agente está disposto a negociar
    quantidade: int  # Quantidade de ativos
    conhecimento: str  # Grau de conhecimento do agente sobre o mercado (ex.: "alto", "médio", "baixo")

    def analisar_mercado(self, mercado: Mercado) -> None:
        """Avalia o mercado e ajusta expectativas e ações baseado no sentimento e conhecimento."""
        print(f"{self.nome} analisando o mercado para o ativo {self.ativo}...")

        # Ajuste de expectativa com base no sentimento
        if self.sentimento == "positivo":
            self.preco = min(
                self.expectativa[2], self.preco * 1.05
            )  # Otimista, aumenta o preço esperado
        elif self.sentimento == "negativo":
            self.preco = max(
                self.expectativa[0], self.preco * 0.95
            )  # Pessimista, reduz o preço esperado
        else:
            self.preco = self.expectativa[
                1
            ]  # Sentimento neutro, segue o preço esperado

        # Uso do conhecimento para tomar decisões mais informadas
        if self.conhecimento == "alto":
            print(
                f"{self.nome} tem conhecimento alto, ajustando expectativas com confiança."
            )
            self.preco += random.uniform(
                -0.5, 0.5
            )  # Pequenos ajustes no preço baseado no conhecimento
        elif self.conhecimento == "baixo":
            print(f"{self.nome} tem conhecimento baixo, decisões mais conservadoras.")
            self.preco += random.uniform(
                -1.0, 1.0
            )  # Ajustes maiores no preço devido à incerteza

    def tomar_decisao(self, mercado: Mercado) -> None:
        """Toma uma decisão de compra ou venda para o ativo específico após análise."""
        # Primeiro o agente analisa o mercado
        self.analisar_mercado(mercado)

        # Toma uma decisão aleatória (compra ou venda) baseada no sentimento e conhecimento
        if random.random() > 0.5:
            print(
                f"{self.nome} decidiu comprar {self.quantidade} de {self.ativo} a {self.preco}"
            )
            mercado.ordem_limitada("compra", self.ativo, self.preco, self.quantidade)
        else:
            print(
                f"{self.nome} decidiu vender {self.quantidade} de {self.ativo} a {self.preco}"
            )
            mercado.ordem_limitada("venda", self.ativo, self.preco, self.quantidade)
