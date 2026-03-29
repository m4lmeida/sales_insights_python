# Funções para calcular faturamento por vendas e total geral.

# CALCULAR O VALOR TOTAL DE UMA VENDA
def calculate_sale_total(sale: list[dict]) -> float:
    return sale["quantity"] * sale["price"]

# CALCULAR O FATURAMENTO TOTAL DE TODAS AS VENDAS
def calculate_total_revenue(sales: list[dict]) -> float:
    total_revenue = 0.0

    for sale in sales:
        total_revenue += calculate_sale_total(sale)

    return total_revenue

# CALCULAR O SUBTOTAL DE CADA VENDAS E RETORNAR UMA LISTA COM ESSES VALORES
def get_sales_totals(sales: list[dict]) -> list[float]:
    totals = []

    for sale in sales:
        totals.append(calculate_sale_total(sale))

    return totals