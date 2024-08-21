from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/dados-seguros', methods=['GET'])
def dados_seguros():
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != 'token':
        return jsonify({'message': 'Acesso não autorizado, token inválido'}), 401
    
    return jsonify({'message': 'Acesso concedido, aqui estão os dados seguros'}), 200

@app.route('/item/<int:item_id>', methods=['GET'])
def obter_item(item_id):
    itens = {1: "Item 1", 2: "Item 2"}
    item = itens.get(item_id)
    
    if not item:
        return jsonify({'message': f'Item com ID {item_id} não encontrado'}), 404
    
    return jsonify({'message': f'Item encontrado: {item}'}), 200

@app.route('/causar-erro', methods=['GET'])
def causar_erro():
    try:
        # Simula um erro no servidor
        1 / 0
    except Exception as e:
        return jsonify({'message': f'Ocorreu um erro inesperado: {str(e)}'}), 500

@app.route('/processar-dados', methods=['POST'])
def processar_dados():
    data = request.get_json()
    if not data or 'key' not in data:
        return jsonify({'message': 'Requisição inválida, chave ausente no JSON'}), 400
    
    return jsonify({'message': 'Dados processados com sucesso'}), 200

@app.route('/criar-item', methods=['POST'])
def criar_item():
    data = request.get_json()
    itens_existentes = ['item1', 'item2']
    
    if data.get('name') in itens_existentes:
        return jsonify({'message': 'Conflito: Item já existe'}), 409
    
    return jsonify({'message': 'Item criado com sucesso'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
