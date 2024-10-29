# Simulação de Mercado de Ativos (Protótipo)

Este projeto é um **esboço de protótipo** de uma simulação de mercado de ativos baseado na bolsa de valores B3. Ele tem como objetivo criar uma simulação simplificada do comportamento de agentes econômicos comprando e vendendo ativos, considerando fatores como sentimento de mercado, expectativas futuras e conhecimento dos agentes.

## Estrutura do Projeto

O projeto está organizado de forma modular, com cada parte da simulação dividida em classes responsáveis por diferentes aspectos do mercado e dos agentes. Abaixo está uma descrição dos principais módulos:

### Módulos

1. **Mercado** (`mercado.py`):
   - Representa o mercado em que os ativos são negociados.
   - Controla os ativos disponíveis e o processamento das ordens.

2. **Agente** (`agente.py`):
   - Representa os agentes participantes do mercado, que podem tomar decisões de compra e venda baseados em seu conhecimento, sentimento e expectativas de preços futuros.
   - Cada agente pode analisar o mercado antes de tomar uma decisão.

3. **Livro de Ordens** (`order_book.py`):
   - Responsável por gerenciar as ordens de compra e venda realizadas pelos agentes.
   - Executa as ordens quando os preços de compra e venda coincidem.

4. **Ordem** (`ordem.py`):
   - Define a estrutura de uma ordem de compra ou venda realizada pelos agentes, com atributos como tipo de ordem, ativo, preço limite e quantidade.

### Simulação

A simulação ocorre em rodadas, onde a cada rodada:

- Os agentes analisam o mercado e tomam decisões de compra ou venda.
- O livro de ordens processa as ordens e executa transações quando possível.
- Ao final de cada rodada, os preços dos ativos são atualizados, e a evolução dos preços é plotada em um gráfico.

### Arquivo Principal

O arquivo principal é `main.py`, onde:

- O mercado e os agentes são inicializados.
- A simulação é executada por várias rodadas.
- Ao final, um gráfico da evolução dos preços dos ativos é gerado.

### Dependências

Este protótipo depende das seguintes bibliotecas Python:

- `matplotlib` para plotar gráficos.
- `numpy` para cálculos numéricos.
- `dataclasses` para definição das estruturas de dados.

Para instalar as dependências, execute:

```bash
pip install matplotlib numpy
```

### Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/Raphael-UFRJ/MestradoMercado.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd MestradoMercado
   ```

3. Execute o arquivo principal:

   ```bash
   python main.py
   ```

### Objetivos Futuros

Este projeto é apenas um **esboço de protótipo** e não reflete uma simulação de mercado totalmente funcional. Possíveis melhorias futuras incluem:

- Implementação de mecanismos mais sofisticados de execução parcial de ordens.
- Simulação mais realista de preços e volumes de negociação.
- Melhor modelagem do comportamento dos agentes, com regras mais avançadas baseadas em dados de mercado.
