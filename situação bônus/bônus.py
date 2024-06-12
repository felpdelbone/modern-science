valor_investido = float(input("Informe valor do investimento: "))
taxa_juros = float(input("Informe a taxa de juros: "))
meses = int(input("Informe o tempo em meses: "))
total = 0  
montante = 0 
print("Informe Qual o tipo do juros ")
escolha_juros = int(input("1 - para juros simples 2 - para juros composto: "))

if escolha_juros == 1 :
    taxa_juros = taxa_juros / 100
    total = valor_investido * taxa_juros * meses
    montante = total + valor_investido

    print("A taxa de juros é de",total)
    print("O montante é de", montante)
else: 
    taxa_juros = taxa_juros / 100

    total = valor_investido * (1+taxa_juros)**meses

    print(total) 