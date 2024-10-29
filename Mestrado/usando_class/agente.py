class Agente():
    def __init__(self, ativo: str, sentimento: str, expectativa: list, preco: float, quantidade: int, tipo: str) -> None:
        self.ativo = ativo
        self.sentimento = sentimento
        self.expectativa = expectativa
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo