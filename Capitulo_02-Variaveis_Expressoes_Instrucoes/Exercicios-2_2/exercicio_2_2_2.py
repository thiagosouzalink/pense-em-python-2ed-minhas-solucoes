"""
Suponha que o preço de capa de um livro seja R$ 24,95, mas as
livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o
primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o
custo total de atacado para 60 cópias?
"""

preco_livro = 24.95
desconto = 40  # %
copias = 60

custo_transporte = 3 + 0.75 * (copias - 1)
custo_compra = (preco_livro - (preco_livro * desconto/100)) * copias
custo_total = custo_transporte + custo_compra

print(f"Custo das compras dos livros: R$ {custo_compra:.2f}")
print(f"Custo total do transporte: R$ {custo_transporte:.2f}")
print(f"Custo total: R$ {custo_total:.2f}")