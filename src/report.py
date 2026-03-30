from datetime import datetime
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_report(
    sales: list[dict],
    total_revenue: float,
    mean_sales: float,
    std_sales: float,
    min_sale: float,
    max_sale: float,
    most_sold_product: str,
    least_sold_product: str,
) -> str:
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    created_at = datetime.now()
    timestamp = created_at.strftime("%Y%m%d_%H%M%S")
    created_at_text = created_at.strftime("%d/%m/%Y %H:%M:%S")

    filename = reports_dir / f"sales_report_{timestamp}.pdf"

    pdf = canvas.Canvas(str(filename), pagesize=A4)
    width, height = A4

    margin_left = 50
    y = height - 50

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(margin_left, y, "Relatório de Vendas")
    y -= 20

    pdf.setFont("Helvetica", 10)
    pdf.drawString(margin_left, y, f"Gerado em: {created_at_text}")
    y -= 30

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(margin_left, y, "Resumo Geral")
    y -= 20

    pdf.setFont("Helvetica", 11)
    pdf.drawString(margin_left, y, f"Quantidade de vendas: {len(sales)}")
    y -= 18
    pdf.drawString(margin_left, y, f"Faturamento total: R$ {total_revenue:.2f}")
    y -= 18
    pdf.drawString(margin_left, y, f"Média das vendas: R$ {mean_sales:.2f}")
    y -= 18
    pdf.drawString(margin_left, y, f"Desvio padrão: R$ {std_sales:.2f}")
    y -= 18
    pdf.drawString(margin_left, y, f"Menor venda: R$ {min_sale:.2f}")
    y -= 18
    pdf.drawString(margin_left, y, f"Maior venda: R$ {max_sale:.2f}")
    y -= 18
    pdf.drawString(margin_left, y, f"Produto mais vendido: {most_sold_product}")
    y -= 18
    pdf.drawString(margin_left, y, f"Produto menos vendido: {least_sold_product}")
    y -= 30

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(margin_left, y, "Detalhamento das Vendas")
    y -= 20

    pdf.setFont("Helvetica", 10)

    for sale in sales:
        sale_total = sale["quantity"] * sale["price"]

        line = (
            f'Produto: {sale["product_name"]} | '
            f'Qtd: {sale["quantity"]} | '
            f'Preço: R$ {sale["price"]:.2f} | '
            f'Total: R$ {sale_total:.2f}'
        )

        pdf.drawString(margin_left, y, line)
        y -= 16

        if y < 50:
            pdf.showPage()
            y = height - 50
            pdf.setFont("Helvetica", 10)

    pdf.save()
    return str(filename)

def save_report_log(report_path: str) -> None:
    logs_dir = Path("reports")
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "report_history.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] PDF gerado: {report_path}\n")