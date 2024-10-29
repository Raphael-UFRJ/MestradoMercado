import timeit


class MercadoClassico:
    def __init__(self, preco, quantidade, tipo, ativo):
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo
        self.ativo = ativo


from dataclasses import dataclass


@dataclass
class MercadoDataclass:
    preco: float
    quantidade: int
    tipo: str
    ativo: str


print(
    "Classe Tradicional:",
    timeit.timeit(
        "MercadoClassico(100.0, 10, 'compra', 'ativo')",
        globals=globals(),
        number=100000,
    ),
)
print(
    "Dataclass:",
    timeit.timeit(
        "MercadoDataclass(100.0, 10, 'compra', 'ativo')",
        globals=globals(),
        number=100000,
    ),
)
