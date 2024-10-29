import matplotlib.pyplot as plt
import random

from usando_dataclass.mercado import Mercado
from usando_dataclass.agente import Agente

def main():
    # Inicializa o mercado e agentes
    mercado = Mercado(preco=100.0, quantidade=100, tipo="compra", ativo="B3")
    agentes = [
        Agente(
            ativo="A",
            sentimento="positivo",
            expectativa=[100, 120],
            preco=random.uniform(95, 105),
            quantidade=random.randint(1, 10),
            tipo="compra",
        )
        for _ in range(10)
    ]

    precos_mercado = []
    rodadas = 20

    # Loop de simulação
    for i in range(rodadas):
        print(f"\nRodada {i+1}")
        for agente in agentes:
            agente.tomar_decisao(mercado)

        mercado.execucao()
        precos_mercado.append(mercado.preco)

    # Plotando o gráfico da evolução do preço
    plt.plot(range(rodadas), precos_mercado, marker="o")
    plt.title("Evolução do Preço do Ativo B3")
    plt.xlabel("Rodadas")
    plt.ylabel("Preço")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
