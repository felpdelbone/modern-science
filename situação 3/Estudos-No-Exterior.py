Capital = float(input("Digite a Montante:"))
Juro_Compostos = float(input("Digite o Valor do Juros:"))
Meses = int(input("Digite a Quantidade de Meses a Montante Ficara Investida:"))

Montante = Capital + ((1 + Juro_Compostos) ** Meses)

print("Ao Final Desse Periodo Você tera acumulado:", Montante)