from dataclasses import dataclass, field
from typing import List
@dataclass
class Ativo:
    nome: str
    preco_atual: float
    historico_precos: List[float] = field(default_factory=list)

    def atualizar_preco(self, novo_preco: float) -> None:
        self.historico_precos.append(self.preco_atual)
        self.preco_atual = novo_preco

    def obter_media_precos(self) -> float:
        """Retorna a média dos preços históricos."""
        return (
            sum(self.historico_precos) / len(self.historico_precos)
            if self.historico_precos
            else self.preco_atual
        )
