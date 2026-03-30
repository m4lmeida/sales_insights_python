# Diretrizes de arquitetura e desenvolvimento

## 1) Visão geral do projeto
- Pequena ferramenta em Python para gerar e resumir registros de vendas aleatórios.
- Fluxo principal: `src/main.py` importa `generate_sales_data()` de `src/sales_data.py`, funções de análise de `src/analytics.py` e geração de relatório de `src/report.py`.
- Arquitetura de processo simples (sem servidor web, sem banco de dados, sem async). Mantenha mudanças nesse pipeline linear, salvo necessidade de refatoração.

## 2) Arquivos principais e responsabilidades
- `src/sales_data.py`: gerador de dados determinístico (`random.seed(30)` garante saída estável), retorna `list[dict]` com campos `product_id`, `product_name`, `quantity`, `price`.
- `src/analytics.py`: funções puras de cálculo e estatística:
  - `calculate_sale_total(sale)` -> float
  - `calculate_total_revenue(sales)` -> float
  - `get_sales_totals(sales)` -> list[float]
  - `calculate_mean_sales(sales)` -> float
  - `calculate_std_sales(sales)` -> float
  - `calculate_min_sale(sales)` -> float
  - `calculate_max_sale(sales)` -> float
  - `get_most_sold_product(sales)` -> str
  - `get_least_sold_product(sales)` -> str
- `src/report.py`: geração de relatório em PDF (usa `reportlab`) e logging de relatórios gerados, mantendo I/O e export separados da lógica analítica.
- `src/main.py`: ponto de entrada que organiza o fluxo, imprime o relatório em stdout, chama a geração do PDF e registra o histórico de relatórios.

## 3) Convenções de formato de dados
- Registro de venda: `{'product_id': int, 'product_name': str, 'quantity': int, 'price': float}`.
- Use esse esquema para novos campos/APIs.

## 4) Comportamentos e detalhes importantes
- `generate_sales_data` usa seed fixa; preserve a determinismo em testes e exemplos.
- Em `main`, os totais e métricas são calculados uma única vez antes da renderização e, em seguida, reutilizados para impressão e geração de relatório.
- A geração de PDF e o registro de relatórios devem permanecer em `src/report.py`; `src/analytics.py` deve continuar livre de I/O.
- O histórico de relatórios gerados é salvo em `reports/report_history.log` e o arquivo PDF fica em `reports/`.

## 5) Fluxo de desenvolvimento esperado
- Ainda não existe suíte de testes; criar testes sob `tests/` para `src/analytics.py` e `src/sales_data.py`.
- Comando de execução: `python src/main.py`.
- Dependências devem incluir `numpy==2.4.4` e, para geração de PDF, `reportlab`.

## 6) Estilo e convenções do projeto
- Anotações de tipo (Type hints) em assinaturas e listas (PEP 585) são preferidas.
- Comentários estão em português; manter o idioma e o mesmo sentido ao adicionar comentários.
- Guardar entrada de módulo com `if __name__ == "__main__":`.

## 7) Orientação para extensões
- Para I/O (CSV/JSON/export), criar `src/io.py` e manter lógica de análise desacoplada.
- Para exportar relatórios, use `src/report.py`; mantenha `src/analytics.py` livre de I/O.
- Mantenha a formatação de saída no `main`; não misture em funções de análise (`analytics.py`).

## 8) Atualização de instruções
- Atualize este arquivo ao adicionar CI/testes.
- Se adicionar workflow do GitHub Actions, inclua `python -m pytest` e comando de lint específicos.