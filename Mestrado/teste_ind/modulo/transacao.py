class Transacao:
    def __init__(self, comprador, vendedor, ativo, quantidade, preco):
        self.comprador = comprador
        self.vendedor = vendedor
        self.ativo = ativo
        self.quantidade = quantidade
        self.preco = preco
        self.realizar_transacao()

    def realizar_transacao(self):
        # Calcular o valor total da transação
        valor_total = self.quantidade * self.preco

        # Verificar se o comprador tem saldo suficiente
        if self.comprador.saldo >= valor_total:
            # Atualizar o saldo e a quantidade de ações do comprador
            self.comprador.saldo -= valor_total
            self.comprador.adicionar_ativo(self.ativo, self.quantidade)

            # Atualizar o saldo e a quantidade de ações do vendedor
            self.vendedor.saldo += valor_total
            self.vendedor.remover_ativo(self.ativo, self.quantidade)

            # Atualizar o preço médio do ativo com base na transação
            self.ativo.atualizar_preco_medio(self.preco)
            print(
                f"Transação realizada: {self.comprador.nome} comprou {self.quantidade} de {self.ativo.nome} de {self.vendedor.nome} a {self.preco}"
            )
        else:
            print(
                f"{self.comprador.nome} não tem fundos suficientes para comprar {self.quantidade} ações de {self.ativo.nome}."
            )
