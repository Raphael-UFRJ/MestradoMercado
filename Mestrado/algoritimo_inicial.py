import random
import matplotlib.pyplot as plt


class Agente:
    def __init__(self, id, nome, saldo, quantidade_acoes):
        self.id = id
        self.nome = nome
        self.saldo = saldo
        self.quantidade_acoes = quantidade_acoes

    def atualizar_saldo_e_acoes(self, quantidade, preco, operacao):
        if operacao == "compra" and self.saldo >= quantidade * preco:
            self.saldo -= quantidade * preco
            self.quantidade_acoes += quantidade
        elif operacao == "venda" and self.quantidade_acoes >= quantidade:
            self.saldo += quantidade * preco
            self.quantidade_acoes -= quantidade
        else:
            print(
                f"Agente {self.nome} não tem recursos suficientes para {operacao} {quantidade} ações."
            )


class Ordem:
    def __init__(self, agente, quantidade, preco, tipo):
        self.agente = agente
        self.quantidade = quantidade
        self.preco = preco
        self.tipo = tipo  # "compra" ou "venda"


class LivroOrdens:
    def __init__(self):
        self.ordens_compra = []
        self.ordens_venda = []

    def adicionar_ordem(self, ordem):
        if ordem.tipo == "compra":
            self.ordens_compra.append(ordem)
            self.ordens_compra.sort(
                key=lambda x: -x.preco
            )  # Ordena por preço descendente
        else:
            self.ordens_venda.append(ordem)
            self.ordens_venda.sort(key=lambda x: x.preco)  # Ordena por preço ascendente

    def executar_transacoes(self):
        transacoes = []
        while self.ordens_compra and self.ordens_venda:
            ordem_compra = self.ordens_compra[0]
            ordem_venda = self.ordens_venda[0]

            if ordem_compra.preco >= ordem_venda.preco:
                preco_execucao = (ordem_compra.preco + ordem_venda.preco) / 2
                quantidade_execucao = min(
                    ordem_compra.quantidade, ordem_venda.quantidade
                )

                ordem_compra.agente.atualizar_saldo_e_acoes(
                    quantidade_execucao, preco_execucao, "compra"
                )
                ordem_venda.agente.atualizar_saldo_e_acoes(
                    quantidade_execucao, preco_execucao, "venda"
                )

                transacoes.append(
                    (
                        ordem_compra.agente,
                        ordem_venda.agente,
                        quantidade_execucao,
                        preco_execucao,
                    )
                )

                ordem_compra.quantidade -= quantidade_execucao
                ordem_venda.quantidade -= quantidade_execucao

                if ordem_compra.quantidade == 0:
                    self.ordens_compra.pop(0)
                if ordem_venda.quantidade == 0:
                    self.ordens_venda.pop(0)
            else:
                break
        return transacoes


def criar_agentes(num_agentes):
    agentes = []
    for i in range(1, num_agentes + 1):
        nome = f"Agente {i}"
        saldo = random.uniform(1000, 5000) if i % 2 == 0 else 0
        quantidade_acoes = random.randint(10, 100) if i % 2 != 0 else 0
        agentes.append(Agente(i, nome, saldo, quantidade_acoes))
    return agentes


def rodadas_negociacao(agentes, num_rodadas):
    livro_ordens = LivroOrdens()
    preco_medio_por_rodada = []
    preco_medio_atual = 0

    for rodada in range(1, num_rodadas + 1):
        print(f"\nRodada {rodada}")

        for agente in agentes:
            if agente.quantidade_acoes > 0:
                preco = random.uniform(20, 50)
                quantidade = random.randint(1, agente.quantidade_acoes)
                ordem = Ordem(agente, quantidade, preco, "venda")
                livro_ordens.adicionar_ordem(ordem)
            elif agente.saldo > 0:
                preco = random.uniform(20, 50)
                quantidade = random.randint(1, int(agente.saldo / preco))
                ordem = Ordem(agente, quantidade, preco, "compra")
                livro_ordens.adicionar_ordem(ordem)

        transacoes = livro_ordens.executar_transacoes()

        if transacoes:
            preco_medio_atual = sum(t[3] for t in transacoes) / len(transacoes)
        preco_medio_por_rodada.append(preco_medio_atual)

        print(f"Preço médio da rodada {rodada}: {preco_medio_atual:.2f}\n")

        print("Book de Ordens:")
        print("Compra:")
        for ordem in livro_ordens.ordens_compra:
            print(
                f"Agente: {ordem.agente.nome}, Quantidade: {ordem.quantidade}, Preço: {ordem.preco:.2f}"
            )
        print("Venda:")
        for ordem in livro_ordens.ordens_venda:
            print(
                f"Agente: {ordem.agente.nome}, Quantidade: {ordem.quantidade}, Preço: {ordem.preco:.2f}"
            )

        print("\nTransações Executadas:")
        for compra, venda, qtd, preco in transacoes:
            print(f"{compra.nome} comprou de {venda.nome} {qtd} ações a R${preco:.2f}")

    return preco_medio_por_rodada


def plotar_grafico(precos_medios):
    plt.plot(range(1, len(precos_medios) + 1), precos_medios, marker="o")
    plt.xlabel("Rodadas")
    plt.ylabel("Preço Médio")
    plt.title("Variação dos Preços Médios ao Longo das Rodadas")
    plt.show()


# Executa a simulação
num_agentes = 10
num_rodadas = 10
agentes = criar_agentes(num_agentes)
precos_medios = rodadas_negociacao(agentes, num_rodadas)
plotar_grafico(precos_medios)
