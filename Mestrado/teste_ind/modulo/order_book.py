from modulo.transacao import Transacao


class OrderBook:
    def __init__(self):
        self.ordens_compra = []
        self.ordens_venda = []

    def adicionar_ordem(self, ordem):
        if ordem.tipo == "compra":
            self.ordens_compra.append(ordem)
        elif ordem.tipo == "venda":
            self.ordens_venda.append(ordem)

    def executar_ordens(self, ativo, mercado):
        self.ordens_compra.sort(key=lambda x: x.preco_limite, reverse=True)
        self.ordens_venda.sort(key=lambda x: x.preco_limite)

        while self.ordens_compra and self.ordens_venda:
            ordem_compra = self.ordens_compra[0]
            ordem_venda = self.ordens_venda[0]

            if ordem_compra.preco_limite >= ordem_venda.preco_limite:
                quantidade_exec = min(ordem_compra.quantidade, ordem_venda.quantidade)
                preco_execucao = (
                    ordem_compra.preco_limite + ordem_venda.preco_limite
                ) / 2

                # Verifica se o comprador tem saldo suficiente
                if ordem_compra.agente.carteira >= quantidade_exec * preco_execucao:
                    transacao = Transacao(
                        comprador=ordem_compra.agente,
                        vendedor=ordem_venda.agente,
                        ativo=ativo,
                        quantidade=quantidade_exec,
                        preco_execucao=preco_execucao,
                    )
                    transacao.executar()

                    # Atualiza as quantidades ou remove as ordens
                    ordem_compra.quantidade -= quantidade_exec
                    ordem_venda.quantidade -= quantidade_exec

                    if ordem_compra.quantidade == 0:
                        self.ordens_compra.pop(0)
                    if ordem_venda.quantidade == 0:
                        self.ordens_venda.pop(0)
                else:
                    print(
                        f"{ordem_compra.agente.nome} não tem fundos suficientes para comprar {quantidade_exec} ações de {ativo}."
                    )
                    break
            else:
                break
