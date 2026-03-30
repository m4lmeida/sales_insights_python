from sales_data import generate_sales_data
from analytics import (
    calculate_sale_total,
    calculate_total_revenue,
    get_sales_totals,
    calculate_mean_sales,
    calculate_std_sales,
    calculate_min_sale,
    calculate_max_sale,
    get_most_sold_product,
    get_least_sold_product,
)
from report import generate_pdf_report, save_report_log


def main() -> None:
    sales = generate_sales_data(10)

    total_revenue = calculate_total_revenue(sales)
    sales_totals = get_sales_totals(sales)
    mean_sales = calculate_mean_sales(sales)
    std_sales = calculate_std_sales(sales)
    min_sale = calculate_min_sale(sales)
    max_sale = calculate_max_sale(sales)
    most_sold_product = get_most_sold_product(sales)
    least_sold_product = get_least_sold_product(sales)

    print("RELATÓRIO DE VENDAS")
    print("-" * 50)

    print("Lista de vendas:")
    for sale in sales:
        sale_total = calculate_sale_total(sale)
        print(
            f'Produto: {sale["product_name"]} | '
            f'Quantidade: {sale["quantity"]} | '
            f'Preço: R$ {sale["price"]:.2f} | '
            f'Total: R$ {sale_total:.2f}'
        )

    print("-" * 50)
    print(f"Quantidade de vendas: {len(sales)}")
    print(f"Totais das vendas: {sales_totals}")
    print(f"Faturamento total: R$ {total_revenue:.2f}")
    print(f"Média das vendas: R$ {mean_sales:.2f}")
    print(f"Desvio padrão das vendas: R$ {std_sales:.2f}")
    print(f"Menor venda: R$ {min_sale:.2f}")
    print(f"Maior venda: R$ {max_sale:.2f}")
    print(f"Produto mais vendido: {most_sold_product}")
    print(f"Produto menos vendido: {least_sold_product}")

    report_path = generate_pdf_report(
        sales=sales,
        total_revenue=total_revenue,
        mean_sales=mean_sales,
        std_sales=std_sales,
        min_sale=min_sale,
        max_sale=max_sale,
        most_sold_product=most_sold_product,
        least_sold_product=least_sold_product,
    )

    save_report_log(report_path)

    print("-" * 50)
    print(f"PDF gerado com sucesso: {report_path}")


if __name__ == "__main__":
    main()