# Calculadora de desconto
valor_prod = float(input('Valor do produto: '))
desc = float(input('Valor do desconto: '))
valor_final = valor_prod * (desc / 100)
print(f'O valor final do produto com desconto é {valor_final:.2f}')