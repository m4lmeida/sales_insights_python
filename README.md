# 📈 Python Sales Reports

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)

Este é um projeto de estudo em Python voltado à geração, análise e exportação de relatórios de vendas. A aplicação cria registros determinísticos, calcula métricas com Python e NumPy e exporta relatórios em PDF com histórico de execução.

## Funcionalidades

- geração determinística de dados de vendas
- cálculo de faturamento total e subtotal por venda
- métricas estatísticas com NumPy
- identificação de produtos mais e menos vendidos
- geração de relatório em PDF
- histórico de relatórios com timestamp

## Tecnologias

- **Python 3.10+**
- **NumPy 2.4.4**
- **ReportLab**
- **Git**
- **GitHub**

## Estrutura do Projeto

```text
sales_insights_python/
├─ docs/
│  ├─ development-guidelines.md
├─ reports/
│  ├─ report_history.log
│  └─ sales_report_<timestamp>.pdf
├─ src/
│  ├─ analytics.py
│  ├─ main.py
│  ├─ report.py
│  └─ sales_data.py
├─ requirements.txt
├─ README.md
├─ LICENSE
└─ .gitignore
````

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/sales_insights_python.git
cd sales_insights_python
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**

```bash
python src/main.py
```

## Formato dos Dados

```json
{
  "product_id": 1,
  "product_name": "Exemplo de Produto",
  "quantity": 5,
  "price": 20.5
}
```

## Saída Gerada

A aplicação:

* exibe o resumo no terminal
* gera um PDF na pasta `reports/`
* registra a execução em `reports/report_history.log`

Exemplo de nome de arquivo:

```text
sales_report_20260329_154530.pdf
```

## Principais Funções

* `calculate_sale_total(sale)`
* `calculate_total_revenue(sales)`
* `get_sales_totals(sales)`
* `get_sales_totals_array(sales)`
* `calculate_mean_sales(sales)`
* `calculate_std_sales(sales)`
* `calculate_min_sale(sales)`
* `calculate_max_sale(sales)`
* `get_most_sold_product(sales)`
* `get_least_sold_product(sales)`

## Contribuições

Contribuições são bem-vindas.

Fluxo sugerido:

```bash
git checkout -b minha-feature
git add .
git commit -m "Descrição da melhoria"
git push origin minha-feature
```

Depois, abra um Pull Request com a proposta de alteração.

## Licença

Este projeto está licenciado sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais detalhes.
