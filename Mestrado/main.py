import random
import matplotlib.pyplot as plt
from usando_dataclass.order_book import OrderBook
from usando_dataclass.mercado import Mercado
from usando_dataclass.agente import Agente


def criar_agentes(num_agentes):
    agentes = []
    ativos = ["PETR4", "VALE3"]
    for i in range(1, num_agentes + 1):
        agente = Agente(
            nome=f"Agente {i}",
            ativo=random.choice(ativos),
            sentimento=random.choice(["positivo", "negativo", "neutro"]),
            expectativa=[
                random.uniform(20, 30),
                random.uniform(25, 35),
                random.uniform(30, 40),
            ],
            preco=random.uniform(25, 35),
            quantidade=random.randint(50, 300),
            conhecimento=random.choice(["alto", "médio", "baixo"]),
            saldo=random.uniform(1000, 10000),
            acoes={ativo: random.randint(0, 1000) for ativo in ativos},
            carteira=0.0,  # Definindo corretamente como um float
        )
        agentes.append(agente)
    return agentes


def main():
    num_agentes = 10
    num_rodadas = 10  # Ajustado para 10 rodadas
    mercado = Mercado(ativos={"PETR4": 50, "VALE3": 45})
    livro_ordens = OrderBook()
    agentes = criar_agentes(num_agentes)

    # Histórico de preços para cada ativo
    historico_precos = {ativo: [] for ativo in mercado.ativos.keys()}

    for rodada in range(1, num_rodadas + 1):
        print(f"\nRodada {rodada}")
        for agente in agentes:
            agente.tomar_decisao(mercado, livro_ordens)

        for ativo in mercado.ativos.keys():
            livro_ordens.executar_ordens(ativo, mercado)
            historico_precos[ativo].append(mercado.ativos[ativo])

    # Plotando o gráfico para 10 rodadas
    plt.figure(figsize=(10, 6))
    for ativo, precos in historico_precos.items():
        plt.plot(range(1, num_rodadas + 1), precos, label=ativo)

    plt.xlabel("Rodadas")
    plt.ylabel("Preço Médio")
    plt.title("Variação dos Preços Médios dos Ativos ao Longo das Rodadas")
    plt.legend()
    plt.xticks(range(1, num_rodadas + 1))  # Define os ticks do eixo x de 1 a 10
    plt.show()


if __name__ == "__main__":
    main()
