import matplotlib.pyplot as plt
from usando_dataclass.mercado import Mercado
from usando_dataclass.agente import Agente
from usando_dataclass.order_book import OrderBook


def main():
    # Inicializando o mercado B3 e o livro de ordens
    mercado_b3 = Mercado()
    livro_ordens = OrderBook()

    # Adicionando ativos na bolsa B3
    mercado_b3.adicionar_ativo("PETR4", 28.50)
    mercado_b3.adicionar_ativo("VALE3", 68.90)

    # Criando agentes que operam no mercado B3
    # Inicialização dos agentes no main.py
    agentes = [
        Agente(
            nome="Agente 1",
            ativo="PETR4",
            sentimento="positivo",
            expectativa=[26, 28, 30],
            preco=28.70,
            quantidade=100,
            conhecimento="alto",
            carteira=5000,  # Exemplo: saldo inicial em reais
            acoes={"PETR4": 0}  # Sem ações inicialmente
        ),
        Agente(
            nome="Agente 2",
            ativo="PETR4",
            sentimento="negativo",
            expectativa=[26, 28, 30],
            preco=28.70,
            quantidade=100,
            conhecimento="alto",
            carteira=5000,  # Exemplo: saldo inicial em reais
            acoes={"PETR4": 100}  # Começa com 100 ações de PETR4
        ),
        # Adicione mais agentes conforme necessário
    ]


    rodadas = 10
    precos_mercado = {  # Armazenar a evolução dos preços dos ativos
        "PETR4": [],
        "VALE3": [],
    }

    # Simulação de mercado
    for rodada in range(rodadas):
        print(f"\nRodada {rodada + 1}")
        for agente in agentes:
            agente.tomar_decisao(
                mercado_b3, livro_ordens
            )  # Passando o mercado e o livro de ordens

        for ativo in mercado_b3.ativos:
            livro_ordens.executar_ordens(ativo)  # Executa as ordens para cada ativo

        # Armazenar os preços dos ativos após cada rodada
        for ativo in mercado_b3.ativos:
            precos_mercado[ativo].append(mercado_b3.ativos[ativo])

    # Plotando o gráfico da evolução do preço dos ativos
    plt.figure(figsize=(10, 5))
    for ativo, precos in precos_mercado.items():
        plt.plot(range(rodadas), precos, marker="o", label=ativo)

    plt.title("Evolução do Preço dos Ativos no Mercado B3")
    plt.xlabel("Rodadas")
    plt.ylabel("Preço")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
