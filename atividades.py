#Atividade Alo Mundo

print("Alo Mundo")


# calculadora de soma 

numero1 = 12
numero2 = 14

soma = numero1 + numero2 

print(soma)


#calculadora de volume

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




     


