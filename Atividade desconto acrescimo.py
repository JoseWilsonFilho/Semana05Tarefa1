dinheiro = float(input())
porcento = float(input())
formula = porcento/100
acrescimo = dinheiro + (dinheiro*formula)
desconto = dinheiro - (dinheiro*formula)
print(f'{acrescimo:.2f}')
print(f'{desconto:.2f}')



