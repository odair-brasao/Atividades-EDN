#Utilizando import

import requests

def consultar_cep(cep):
    cep = cep.replace("-","").strip()
    if len(cep) != 8 or not cep.isdigit():
        print("Cep invalido. Digite um cep com 8 números")
        return
    
    url = f"https://viacep.com.br/ws/%7Bcep%7D/json/"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print("Erro ao acessar a API via CEP")
        return
    
    dados = resposta.jason()


    if "erro" in dados:
        print("Cep não encontrado")
        return
    
    
    print("\n Endereço encontrado:")
    print(f"Logradouro: {dados.get("logradouro")}")
    print(f"Bairro: {dados.get("bairro")}")
    print(f"Cidade: {dados.get("cidade")}")
    print(f"Estados {dados.get("uf")}")

cep_usuario = input("Digite o CEP: ")
consultar_cep(cep_usuario)
