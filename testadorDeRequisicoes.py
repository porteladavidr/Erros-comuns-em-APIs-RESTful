import requests

def test_dados_seguros():
    print("Teste: /dados-seguros (GET)")
    token = input("Digite o token (ou deixe em branco para inválido): ")
    headers = {'Authorization': f'{token}'} if token else {}
    response = requests.get('http://localhost:5000/dados-seguros', headers=headers)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())
    print()

def test_obter_item():
    print("Teste: /item/<int:item_id> (GET)")
    item_id = input("Digite o ID do item: ")
    response = requests.get(f'http://localhost:5000/item/{item_id}')
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())
    print()

def test_causar_erro():
    print("Teste: /causar-erro (GET)")
    response = requests.get('http://localhost:5000/causar-erro')
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())
    print()

def test_processar_dados():
    print("Teste: /processar-dados (POST)")
    key_value = input("Digite o valor para 'key' (ou deixe em branco para inválido): ")
    data = {'key': key_value} if key_value else {}
    response = requests.post('http://localhost:5000/processar-dados', json=data)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())
    print()

def test_criar_item():
    print("Teste: /criar-item (POST)")
    name = input("Digite o nome do item (ou digite item1 ou item2 para validação correta): ")
    data = {'name': name}
    response = requests.post('http://localhost:5000/criar-item', json=data)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())
    print()

def main():
    while True:
        print("Escolha o teste a ser realizado:")
        print("1: Testar /dados-seguros (GET)")
        print("2: Testar /item/<int:item_id> (GET)")
        print("3: Testar /causar-erro (GET)")
        print("4: Testar /processar-dados (POST)")
        print("5: Testar /criar-item (POST)")
        print("0: Sair")
        choice = input("Digite o número da opção desejada: ")
        
        if choice == '1':
            test_dados_seguros()
        elif choice == '2':
            test_obter_item()
        elif choice == '3':
            test_causar_erro()
        elif choice == '4':
            test_processar_dados()
        elif choice == '5':
            test_criar_item()
        elif choice == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
