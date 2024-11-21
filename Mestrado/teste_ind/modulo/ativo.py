class Ativo:
    def __init__(self, nome, preco_inicial):
        self.nome = nome
        self.preco_medio = preco_inicial
        self.historico_precos = [preco_inicial]  # Manter um histórico dos preços

    def atualizar_preco_medio(self, novo_preco):
        self.historico_precos.append(novo_preco)
        self.preco_medio = sum(self.historico_precos) / len(
            self.historico_precos
        )  # Calcular o preço médio
