# transacao.py
from dataclasses import dataclass
from .agente import Agente


@dataclass
class Transacao:
    comprador: Agente
    vendedor: Agente
    ativo: str
    quantidade: int
    preco_execucao: float

    def executar(self):
        valor_total = self.quantidade * self.preco_execucao

        if isinstance(self.comprador.carteira, float) and isinstance(
            self.vendedor.carteira, float
        ):
            self.comprador.carteira -= valor_total
            self.vendedor.carteira += valor_total
            self.comprador.ativos[self.ativo] += self.quantidade
            self.vendedor.ativos[self.ativo] -= self.quantidade
        else:
            print(
                f"Erro ao executar transação: 'carteira' deve ser do tipo float para {self.comprador.nome} e {self.vendedor.nome}."
            )
