print("Desconto 10% em 3 produtos, calcule o preço final")
def desconto_produto(product):
    result = product - (product * 0.10)
    print(f"O preço do produto {product:.2f} com desconto de 10% é: {result:.2f}\n")

desconto_produto(50.00)
desconto_produto(120.00)
desconto_produto(200.00)
