#Atividade Alo Mundo

print("Alo Mundo")


# Calculadora de soma 

numero1 = 12
numero2 = 14

soma = numero1 + numero2 

print(soma)


#Calculadora de volume

def calcular_volume_caixa(comprimento, largura, altura):
    volume = comprimento * largura * altura
    return volume


try:
    comprimento = float(input("Digite o comprimento da caixa"))
    largura = float(input("Digite a largura da caixa"))
    altura = float(input("Digite a altura da caixa"))

    volume_total = calcular_volume_caixa(comprimento, largura, altura)

    print(f"O volume da caixa é: {volume_total: .2f}.") 

except ValueError:
       print("Erro: Por favor insira apenas numeros validos ")

#Calculadora de preço

def calcular_valor_compra(valor, quantidade):
    valor = valor * quantidade
    return valor


try:
    valor = float(input("Digite o valor do produto"))
    quantidade = float(input("Digite a quantidade"))
    

    valor = calcular_valor_compra(valor, quantidade)

    print(f"O volume da compra é: {valor:.2f}:") 

except ValueError:
       print("Erro: Por favor insira apenas numeros validos ")


       #Convesor de Moeda
      
def converso_moedas(valor_reais, taxa_dolar, taxa_euro):
    valordolar = valor_reais / taxa_dolar
    valoreuro = valor_reais / taxa_euro
    return (valordolar , valoreuro)

     
try:
    valor_reais = float(input("Digite o valor em reais: "))
    taxa_dolar = 5.20
    taxa_euro = 6.15

    valordolar = valor_reais / taxa_dolar
    valoreuro = valor_reais / taxa_euro


    print(f"Valor investido em reais {valor_reais:.2f}:")
    print(f"Valor convertido dolar{valordolar:.2f}:")
    print(f"Valor convertido euro{valoreuro:.2f}:")

except ValueError:
     
     print("Erro: Por favor insira um valor valido.")



          



     


