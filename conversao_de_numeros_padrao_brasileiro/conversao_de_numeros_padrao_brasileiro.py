
# Fazendo o python interpretar números do padrão brasileiro, fazer operações com eles no padrão internacional [...]
# e no final, responder com números no padrão brasileiro

num1 = str(input('Digite qualquer número, podendo ser inteiro ou decimal: '))
num2 = str(input('Digite outro número: '))

# Transformações de números de padrões brasileiros em padrões internacionais
num1 = num1.replace('.','').replace(',','.')
num1_int = float(num1)
num2 = num2.replace('.','').replace(',','.')
num2_int = float(num2)

# Operações entre os dois números em padrão internacional
soma = num1_int + num2_int
sub = num1_int + num2_int
multi = num1_int * num2_int
div = num1_int / num2_int

# Transformando todos esses resultados no padrão brasileiro
somabr = f'{soma:_.2f}'
somabr = somabr.replace('.',',').replace('_','.')
subbr = f'{sub:_.2f}'
subbr = subbr.replace('.',',').replace('_','.')
multibr = f'{multi:_.2f}'
multibr = multibr.replace('.',',').replace('_','.')
divbr = f'{div:_.2f}'
divbr = divbr.replace('.',',').replace('_','.')

# Mostrando na tela todos os resultados em valores do padrão brasileiro
print(f'Soma: {somabr}\nSubtração: {subbr}\nMultiplicação: {multibr}\nDivisão: {divbr}')
# Atenção: Nesses cálculos, usei aproximações de duas casas decimais
