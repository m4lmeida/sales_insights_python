import numpy as np

# CALCULAR O VALOR TOTAL DE UMA VENDA
def calculate_sale_total(sale: dict) -> float:
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

# TRANFORMAR A LISTA DE VENDAS EM UM ARRAY DO NUMPY
def get_sales_totals_array(sales: list[dict]) -> np.ndarray:
    totals = get_sales_totals(sales)
    return np.array(totals, dtype=float)

# CALCULAR A MÉDIA DE FATURAMENTO
def calculate_mean_sales(sales: list[dict]) -> float:
    totals_array = get_sales_totals_array(sales)
    return float(np.mean(totals_array))

# CALCULAR O DESVIO PADRÃO DO FATURAMENTO
def calculate_std_sales(sales: list[dict]) -> float:
    totals_array = get_sales_totals_array(sales)
    return float(np.std(totals_array))

# CALCULAR VALOR MÍNIMO DE FATURAMENTO
def calculate_min_sale(sales: list[dict]) -> float:
    totals_array = get_sales_totals_array(sales)
    return float(np.min(totals_array))

# CALCULAR O VALOR MÁXIMO DE FATURAMENTO
def calculate_max_sale(sales: list[dict]) -> float:
    totals_array = get_sales_totals_array(sales)
    return float(np.max(totals_array))

# CHECAR PRODUTO MAIS VENDIDO
def get_most_sold_product(sales: list[dict]) -> str:
    product_sales = {}

    for sale in sales:
        product = sale['product_name']
        quantity = sale['quantity']

        if product in product_sales:
            product_sales[product] += quantity
        else:
            product_sales[product] = quantity

    most_sold_product = max(product_sales, key=product_sales.get)
    return most_sold_product    

# CHECAR PRODUTO MENOS VENDIDO
def get_least_sold_product(sales: list[dict]) -> str:
    product_sales = {}
    
    for sale in sales:
        product = sale['product_name']
        quantity = sale['quantity']

        if product in product_sales:
            product_sales[product] += quantity
        else:
            product_sales[product] = quantity

    least_sold_product = min(product_sales, key=product_sales.get)
    return least_sold_product