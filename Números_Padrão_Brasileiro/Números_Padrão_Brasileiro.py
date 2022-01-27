
# Fazendo o python interpretar números do padrão brasileiro, fazer operações com eles no padrão internacional [...]
# e no final, responder com números no padrão brasileiro

a = str(input('Me diga qualquer número, podendo ser inteiro ou decimal: '))
b = str(input('Me diga outro número: '))

# Transformações de números de padrões brasileiros em padrões internacionais
a = a.replace('.','').replace(',','.')
a1 = float(a)
b = b.replace('.','').replace(',','.')
b1 = float(b)

# Operações entre os dois números em padrão internacional
soma = a1+b1
sub = a1-b1
multi = a1*b1
div = a1/b1

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
