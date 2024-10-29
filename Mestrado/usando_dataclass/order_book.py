from dataclasses import dataclass, field
from typing import List
from .ordem import Ordem


@dataclass
class OrderBook:
    ordens_compra: List[Ordem] = field(default_factory=list)
    ordens_venda: List[Ordem] = field(default_factory=list)

    def adicionar_ordem(self, ordem: Ordem) -> None:
        if ordem.tipo_ordem == "compra":
            self.ordens_compra.append(ordem)
        elif ordem.tipo_ordem == "venda":
            self.ordens_venda.append(ordem)

    def obter_melhor_preco_compra(self, ativo: str) -> float:
        compras_do_ativo = [
            ordem for ordem in self.ordens_compra if ordem.ativo == ativo
        ]
        if compras_do_ativo:
            return max(ordem.preco_limite for ordem in compras_do_ativo)
        return None

    def obter_melhor_preco_venda(self, ativo: str) -> float:
        vendas_do_ativo = [ordem for ordem in self.ordens_venda if ordem.ativo == ativo]
        if vendas_do_ativo:
            return min(ordem.preco_limite for ordem in vendas_do_ativo)
        return None

    def executar_ordens(self, ativo: str) -> None:
        """Executa as ordens de compra e venda, se possível."""
        melhor_preco_compra = self.obter_melhor_preco_compra(ativo)
        melhor_preco_venda = self.obter_melhor_preco_venda(ativo)

        if (
            melhor_preco_compra
            and melhor_preco_venda
            and melhor_preco_compra >= melhor_preco_venda
        ):
            print(
                f"Executando ordens para {ativo} entre {melhor_preco_compra} e {melhor_preco_venda}"
            )

            ordens_compra_executadas = []
            ordens_venda_executadas = []

            for ordem_compra in self.ordens_compra:
                if (
                    ordem_compra.ativo == ativo
                    and ordem_compra.preco_limite == melhor_preco_compra
                ):
                    print(
                        f"Executando {ordem_compra.quantidade} unidades de {ativo} a {ordem_compra.preco_limite}"
                    )
                    ordens_compra_executadas.append(ordem_compra)

            for ordem_venda in self.ordens_venda:
                if (
                    ordem_venda.ativo == ativo
                    and ordem_venda.preco_limite == melhor_preco_venda
                ):
                    print(
                        f"Executando {ordem_venda.quantidade} unidades de {ativo} a {ordem_venda.preco_limite}"
                    )
                    ordens_venda_executadas.append(ordem_venda)

            # Remover as ordens executadas da lista
            for ordem_compra in ordens_compra_executadas:
                if ordem_compra in self.ordens_compra:
                    self.ordens_compra.remove(ordem_compra)

            for ordem_venda in ordens_venda_executadas:
                if ordem_venda in self.ordens_venda:
                    self.ordens_venda.remove(ordem_venda)
        else:
            print(f"Sem execução para {ativo}")
