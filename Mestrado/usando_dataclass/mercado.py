from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Mercado:
    bolsa: str = "B3"
    ativos: Dict[str, float] = field(
        default_factory=lambda: {"PETR4": 50.0, "VALE3": 45.0}
    )  # Ativos sendo negociados com seus preços, dois ativos padrões com seus preços iniciais
    book: Dict[str, List[Dict[str, float]]] = field(default_factory=dict)

    def __repr__(self) -> str:
        return f"Mercado(Bolsa: {self.bolsa}, Ativos: {self.ativos})"

    def __str__(self) -> str:
        return f"Mercado(Bolsa: {self.bolsa}, Ativos: {self.ativos})"

    def adicionar_ativo(self, nome_ativo: str, preco_inicial: float) -> None:
        """Adiciona um ativo ao mercado com o preço inicial."""
        self.ativos[nome_ativo] = preco_inicial

    def ordem_limitada(
        self, tipo_ordem: str, ativo: str, preco_limite: float, quantidade: int
    ) -> None:
        """Adiciona uma ordem limitada para um ativo no mercado."""
        if tipo_ordem not in self.book:
            self.book[tipo_ordem] = []
        self.book[tipo_ordem].append(
            {"ativo": ativo, "preco": preco_limite, "quantidade": quantidade}
        )
        print(
            f"Ordem Limitada adicionada: {tipo_ordem} {quantidade} de {ativo} a {preco_limite}"
        )

    def atualizar_preco(self, ativo: str, novo_preco: float):
        """Atualiza o preço de um ativo no mercado."""
        self.ativos[ativo] = novo_preco

    def execucao(self) -> None:
        """Executa as ordens limitadas se houver coincidência de preços."""
        for ativo in self.ativos:
            if "compra" in self.book and "venda" in self.book:
                ordens_compra = [
                    ordem for ordem in self.book["compra"] if ordem["ativo"] == ativo
                ]
                ordens_venda = [
                    ordem for ordem in self.book["venda"] if ordem["ativo"] == ativo
                ]

                if ordens_compra and ordens_venda:
                    melhor_preco_compra = max(ordem["preco"] for ordem in ordens_compra)
                    melhor_preco_venda = min(ordem["preco"] for ordem in ordens_venda)

                    # Somente executa se o preço de compra for maior ou igual ao preço de venda
                    if melhor_preco_compra >= melhor_preco_venda:
                        # Ajusta o preço do ativo como a média dos melhores preços de compra e venda
                        self.ativos[ativo] = (
                            melhor_preco_compra + melhor_preco_venda
                        ) / 2
                        print(f"Preço ajustado para {ativo}: {self.ativos[ativo]}")

                        # Remove as ordens que foram executadas
                        self.book["compra"] = [
                            ordem
                            for ordem in self.book["compra"]
                            if ordem["preco"] != melhor_preco_compra
                        ]
                        self.book["venda"] = [
                            ordem
                            for ordem in self.book["venda"]
                            if ordem["preco"] != melhor_preco_venda
                        ]
                    else:
                        print(
                            f"Sem execução para o ativo {ativo} (melhor preço de compra < melhor preço de venda)"
                        )
                else:
                    print(f"Sem ordens de compra ou venda para executar para {ativo}.")
