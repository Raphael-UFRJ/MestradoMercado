import random
import matplotlib.pyplot as plt
from modulo.order_book import OrderBook
from modulo.ordem import Ordem
from modulo.mercado import Mercado
from modulo.agente import Agente


def criar_agentes(num_agentes):
    agentes = []
    for i in range(1, num_agentes + 1):
        agente = Agente(
            nome=f"Agente {i}",
            saldo_inicial=10000,  # Por exemplo, cada agente começa com um saldo inicial de 10.000
        )
        agentes.append(agente)
    return agentes


def main():
    num_agentes = 10
    num_rodadas = 10
    mercado = Mercado(ativos={"PETR4": 50, "VALE3": 45})
    livro_ordens = OrderBook()
    agentes = criar_agentes(num_agentes)

    historico_precos = {ativo: [] for ativo in mercado.ativos.keys()}

    for rodada in range(1, num_rodadas + 1):
        print(f"\nRodada {rodada}")
        for agente in agentes:
            agente.tomar_decisao(mercado, livro_ordens)

        for ativo in mercado.ativos.keys():
            livro_ordens.executar_ordens(ativo, mercado)
            historico_precos[ativo].append(mercado.ativos[ativo])

    # Plot do histórico de preços dos ativos
    plt.figure(figsize=(10, 6))
    for ativo, precos in historico_precos.items():
        plt.plot(range(1, num_rodadas + 1), precos, label=ativo)

    plt.xlabel("Rodadas")
    plt.ylabel("Preço Médio")
    plt.title("Variação dos Preços Médios dos Ativos ao Longo das Rodadas")
    plt.legend()
    plt.show()

    # Exibir saldo final de cada agente
    print("\nSaldo final de cada agente:")
    for agente in agentes:
        print(f"{agente.nome} - Saldo final: R${agente.carteira:.2f}")

    # Exibir valor final de cada ativo
    print("\nValor final de cada ativo:")
    for ativo, preco in mercado.ativos.items():
        print(f"{ativo}: R${preco:.2f}")


if __name__ == "__main__":
    main()
