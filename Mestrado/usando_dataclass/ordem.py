from dataclasses import dataclass

@dataclass
class Ordem:
    tipo_ordem: str  # "compra" ou "venda"
    ativo: str
    preco_limite: float
    quantidade: int 
    quantidade_executada: int = 0

    def __repr__(self):
        return f"Ordem({self.tipo_ordem}, {self.ativo}, {self.preco_limite}, {self.quantidade}, Executada: {self.quantidade_executada})"

    def restante(self) -> int:
        """Retorna a quantidade restante a ser executada."""
        return self.quantidade - self.quantidade_executada

    def is_fully_executed(self) -> bool:
        """Verifica se a ordem foi totalmente executada."""
        return self.quantidade_executada >= self.quantidade
