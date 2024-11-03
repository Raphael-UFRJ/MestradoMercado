# Imports
from dataclasses import dataclass, field
from typing import Dict, List
import random
from .mercado import Mercado
from .ordem import Ordem
import numpy as np


@dataclass
class Agente:
    nome: str
    ativo: str
    saldo: float  # Saldo em dinheiro
    sentimento: str  # "positivo", "negativo" ou "neutro"
    expectativa: List[float]  # [preço mínimo, preço esperado, preço máximo]
    preco: float  # Preço atual que o agente está disposto a negociar
    quantidade: int  # Quantidade de ativos
    conhecimento: str  # "alto", "médio", "baixo"
    carteira: float = 0.0  # Inicialize como um float
    acoes: Dict[str, int] = field(
        default_factory=dict
    )  # Quantidade de ações de cada ativo
    ativos: Dict[str, int] = field(default_factory=dict)  # Ativos com valor padrão

    def __post_init__(self):
        # Inicializa saldo e ativos
        # Garante que 'carteira' seja sempre um float
        self.carteira = float(self.carteira)
        self.saldo = random.uniform(1000, 10000)  # Saldo inicial aleatório
        self.ativos = {"PETR4": 0, "VALE3": 0}

    def analisar_mercado(self, mercado: Mercado) -> None:
        """Avalia o mercado e ajusta expectativas e ações baseado no sentimento e conhecimento."""
        print(f"{self.nome} analisando o mercado para o ativo {self.ativo}...")
        media_preco = np.mean(list(mercado.ativos.values()))
        desvio_padrao = np.std(list(mercado.ativos.values()))
        print(
            f"Analisando mercado, preço médio: {media_preco}, desvio padrão: {desvio_padrao}"
        )

        # Ajuste de expectativa com base no sentimento
        if self.sentimento == "positivo":
            self.preco = min(
                self.expectativa[2], self.preco * random.uniform(1.05, 1.15)
            )
        elif self.sentimento == "negativo":
            self.preco = max(
                self.expectativa[0], self.preco * random.uniform(0.85, 0.95)
            )
        else:
            self.preco = self.expectativa[1] + random.uniform(-0.5, 0.5)

        # Ajuste baseado no conhecimento
        if self.conhecimento == "alto":
            self.preco += random.uniform(-0.8, 0.8)
        elif self.conhecimento == "baixo":
            self.preco += random.uniform(-1.5, 1.5)

    def tomar_decisao(self, mercado: Mercado, order_book) -> None:
        """Decide se o agente irá comprar ou vender ativos com base nas condições de mercado."""
        for ativo, preco_mercado in mercado.ativos.items():
            # Decide se o agente vai comprar ou vender com base em uma probabilidade
            acao = "compra" if random.random() > 0.5 else "venda"
            quantidade = random.randint(10, 100)  # Quantidade aleatória para a ordem
            preco_limite = preco_mercado * (1 + random.uniform(-0.05, 0.05))

            # Cria a ordem de acordo com a ação decidida
            ordem = Ordem(
                tipo=acao,  # Use 'tipo' para corresponder ao campo esperado na classe Ordem
                agente=self,
                ativo=ativo,
                quantidade=quantidade,
                preco_limite=preco_limite,
            )

            order_book.adicionar_ordem(ordem)

            # Mensagem de feedback para ver o que foi criado
            print(
                f"{self.nome} enviou uma ordem de {acao.upper()} de {quantidade} de {ativo} a {preco_limite:.2f}"
            )
