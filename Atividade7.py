nome = input("Nome do desgraçado: ")
venda = input("Valor das vendas: ")
salario = input("Salario do miserável: ")
salint = int(salario)
venflo = float(venda)
comisão = (venflo / 100) * 15
total = comisão + salint
print("Total = R$ ",total)
