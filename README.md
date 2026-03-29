# Sales Insights 📈

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)

Este é um projeto de estudo em Python focado em processamento de dados e lógica de análise de vendas. A ferramenta gera registros de vendas aleatórios e fornece um resumo detalhado da receita e performance dos produtos.

---

## ✨ Funcionalidades

- **Geração de dados determinística:** cria listas de vendas com campos de ID, nome, quantidade e preço, garantindo resultados consistentes através de uma semente fixa (`seed`).
- **Cálculos analíticos:** processamento de totais por venda e receita total acumulada.
- **Relatório via terminal:** exibição organizada dos dados processados diretamente no console (`stdout`).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python](https://www.python.org/) com uso de Type Hints (PEP 585)
- **Biblioteca de dados:** [NumPy](https://numpy.org/) (`numpy==2.4.4`)
- **Controle de versão:** [Git](https://git-scm.com/)
- **Hospedagem de código:** [GitHub](https://github.com/)

---

## 📂 Estrutura do Projeto

A aplicação segue uma arquitetura modular para separar a lógica de dados da lógica de negócio:

- `src/sales_data.py`: responsável pela geração da lista de dicionários de vendas
- `src/analytics.py`: contém as funções puras de cálculo matemático, como receita total e totais por venda
- `src/main.py`: ponto de entrada da aplicação, responsável por coordenar o fluxo e exibir o relatório

```text
sales_insights/
├─ .venv/
├─ src/
│  ├─ analytics.py
│  ├─ main.py
│  └─ sales_data.py
├─ requirements.txt
├─ README.md
├─ LICENSE
└─ .gitignore
````

---

## ⚙️ Como Executar o Projeto Localmente

### Pré-requisitos

* Python 3.10 ou superior instalado
* Git instalado

### Passo a passo

1. **Clone o repositório:**

```bash
git clone https://github.com/SEU-USUARIO/sales_insights_python
cd sales_insights_python
```

2. **Crie um ambiente virtual:**

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

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**

```bash
python src/main.py
```

---

## 🔌 Formato dos Dados

Os registros seguem o seguinte esquema:

```json
{
  "product_id": 1,
  "product_name": "Exemplo de Produto",
  "quantity": 5,
  "price": 20.5
}
```

---

## 🖥️ Exemplo de Saída no Terminal

```text
RELATÓRIO INICIAL DE VENDAS
------------------------------
LISTA DE VENDAS:
Produto: Product_70 | Quantidade: 5 | Preço: $ 37.61 | Total: $ 188.05
Produto: Product_79 | Quantidade: 2 | Preço: $ 31.74 | Total: $ 63.48
Produto: Product_4 | Quantidade: 8 | Preço: $ 79.68 | Total: $ 637.44
------------------------------
Subtotais das vendas: [188.05, 63.48, 637.44]
Faturamento total: $ 888.97
```

---

## 🧮 Lógica Atual de Análise

Atualmente o projeto implementa:

### `calculate_sale_total(sale)`

Calcula o total de uma venda individual:

```python
total = sale["quantity"] * sale["price"]
```

### `calculate_total_revenue(sales)`

Percorre todas as vendas e acumula o faturamento total.

### `get_sales_totals(sales)`

Cria uma nova lista contendo o total de cada venda.

---

## 📦 Dependências

O projeto utiliza atualmente:

```text
numpy==2.4.4
```

---

## 🧪 Testes

Ainda não há uma suíte de testes implementada.

Quando os testes forem adicionados, a execução esperada será:

```bash
python -m pytest
```

---

## 🔄 Versionamento com Git e GitHub

### Inicializar o repositório Git

```bash
git init
git add .
git commit -m "Projeto inicial sales_insights"
```

### Conectar ao GitHub

Crie um repositório no GitHub e depois conecte o projeto local:

```bash
git remote add origin https://github.com/SEU-USUARIO/sales_insights_python
git branch -M main
git push -u origin main
```

### Fluxo básico para atualizações futuras

Sempre que fizer alterações no projeto:

```bash
git add .
git commit -m "Descrição da melhoria realizada"
git push
```

Exemplo:

```bash
git add .
git commit -m "Adiciona cálculo de ticket médio"
git push
```

---

## 🧭 Convenções do Projeto

* Comentários e documentação em português
* Uso de Type Hints nas assinaturas
* Estruturas tipadas com `list[dict]` no padrão PEP 585
* Lógica de análise desacoplada da saída
* Entrada principal protegida por:

```python
if __name__ == "__main__":
    main()
```

---

## 📚 Aprendizados Envolvidos

Este projeto serve como base para evoluir futuramente para temas como:

* leitura de CSV com Python
* análise com NumPy e pandas
* geração de relatórios mais completos
* visualização de dados
* testes automatizados
* boas práticas de versionamento com Git e GitHub

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**.

Você pode usar, modificar, distribuir e adaptar este projeto livremente, desde que mantenha o aviso de copyright e a licença original.

Para mais detalhes, consulte o arquivo `LICENSE`.
