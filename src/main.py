# GERAR RELATÓRIO DE VENDAS

from sales_data import generate_sales_data
from analytics import calculate_total_revenue, get_sales_totals, calculate_sale_total

def main() -> None:
    sales: list[dict] = generate_sales_data(30)
    
    print("RELATÓRIO INICIAL DE VENDAS")
    print("-" * 30)

    print("LISTA DE VENDAS:")
    for sale in sales:
        total = calculate_sale_total(sale)
        print(
            f'Produto: {sale["product_name"]} | ' 
            f'Quantidade: {sale["quantity"]} | '
            f'Preço: ${sale["price"]:.2f} | '
            f'Total: ${total:.2f}'
        )

        total_revenue = calculate_total_revenue(sales)
        sales_totals = get_sales_totals(sales)

    print("-" * 30)
    print(f'Subtotais das vendas: {sales_totals}')
    print(f'Faturamento total: ${total_revenue:.2f}')

if __name__ == "__main__":
    main()