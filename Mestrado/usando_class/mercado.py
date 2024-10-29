class Mercado(object):
    def __init__(self, preco: float, quantidade: int, tipo: str, ativo) -> None:
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo
        self.ativo = ativo
        self.book: str = None

    def __repr__(self) -> str:
        return f"Mercado({self.preco}, {self.quantidade}, {self.tipo}, {self.ativo})"

    def __str__(self) -> str:
        return f"Mercado(Preço: {self.preco}, Quantidade: {self.quantidade}, Tipo: {self.tipo}, Ativo: {self.ativo})"

    def ordem_limitada(self, book: str) -> None:
        ...
    
    def ordem_a_mercado(self) -> None:
        ...
    
    def execucao(self) -> None:
        ...