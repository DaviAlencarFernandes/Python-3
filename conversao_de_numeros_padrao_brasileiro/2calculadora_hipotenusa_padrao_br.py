import math
cat1 = str(input('Me diga o valor de um dos catetos: '))
cat2 = str(input('Me diga o valor do outro cateto: '))
cat1 = cat1.replace('.', '').replace(',','.')
cat1 = float(cat1)
cat2 = cat2.replace('.', '').replace(',','.')
cat2 = float(cat2)
h = math.sqrt(pow(cat1, 2) + pow(cat2, 2))
texto_h = f'{h:_.2f}'
hbr = texto_h.replace('.', ',').replace('_', '.')
print(f'A hipotenusa é: {hbr}\nAtenção: Aproximação de duas casas decimais')