# Sales Insights 📈

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)

Este é um projeto de estudo em Python focado em processamento de dados e lógica de análise de vendas. A ferramenta gera registros de vendas aleatórios e fornece um resumo detalhado da receita e performance dos produtos.

---

## ✨ Funcionalidades

- [cite_start]**Geração de Dados Determinística:** Cria listas de vendas com campos de ID, nome, quantidade e preço, garantindo resultados consistentes através de uma semente fixa (`seed`).
- [cite_start]**Cálculos Analíticos:** Processamento de totais por venda e receita total acumulada[cite: 2].
- [cite_start]**Relatório via Terminal:** Exibição organizada dos dados processados diretamente no console (stdout)[cite: 2].

---

## 🛠️ Tecnologias Utilizadas

- [cite_start]**Linguagem:** [Python](https://www.python.org/) (utilizando Type Hints - PEP 585)[cite: 6].
- [cite_start]**Biblioteca de Dados:** [Numpy](https://numpy.org/) (versão 2.4.4).

---

## 📂 Estrutura do Projeto

[cite_start]A aplicação segue uma arquitetura modular para separar a lógica de dados da lógica de negócio[cite: 2]:

- [cite_start]`src/sales_data.py`: Responsável pela geração da lista de dicionários de vendas[cite: 2].
- [cite_start]`src/analytics.py`: Contém as funções puras de cálculo matemático (Receita Total, Totais por Venda)[cite: 2].
- [cite_start]`src/main.py`: Ponto de entrada da aplicação que coordena o fluxo e exibe o relatório[cite: 2].

---

## ⚙️ Como Executar o Projeto Localmente

### Pré-requisitos
- Python 3.10 ou superior instalado.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/sales_insights.git](https://github.com/SEU-USUARIO/sales_insights.git)
   cd sales_insights

2. Crie um ambiente virtual (recomendado):

Bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

3. Instale as dependências:

Bash
pip install -r requirements.txt

4. Execute a aplicação:

Bash
python src/main.py

---

## 🔌 Exemplo de Saída (Data Format)
Os registros seguem o seguinte esquema de dados:

JSON
{
  "product_id": 1,
  "product_name": "Exemplo de Produto",
  "quantity": 5,
  "price": 20.5
}

---

## 💡 Instruções de Implementação

1.  **Ficheiro `requirements.txt`**: Certifica-te de que tens este ficheiro na raiz com o conteúdo `numpy==2.4.4`, conforme as tuas instruções.
2.  **Organização de Pastas**: Garante que os teus ficheiros estão dentro da pasta `src/` para que o comando de execução sugerido no README funcione corretamente.
3.  **Documentação**: Como o teu projeto usa **Type Hints**, o código já será naturalmente mais fácil de ler, o que é excelente para o teu portfólio no GitHub![cite: 6].

Precisas de ajuda para configurar o ficheiro de testes `pytest` que mencionaste no roadmap?