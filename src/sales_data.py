# Simulação de dados de vendas utilizando função de geração de dados aleatórios.

import random

def generate_sales_data(num_records: int) -> list[dict]:
    sales_data = []

    random.seed(30)  # Para garantir resultados consistentes  

    for _ in range(num_records):
        product_id = random.randint(1, 100)
        product_name = f"Product_{product_id}"
        quantity = random.randint(1, 10)
        price = round(random.uniform(10.0, 100.0), 2)

        sale = {
            "product_id": product_id,
            "product_name": product_name,
            "quantity": quantity,
            "price": price,
        }

        sales_data.append(sale)

    return sales_data