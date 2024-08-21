# API Flask apiErrosComunsApi

**Descrição:**

Esta API Flask simples demonstra diversos endpoints e tratamentos de erros comuns em APIs RESTful.

## Endpoints da API

* **GET /dados-seguros:**
  * Retorna dados seguros após autenticação.
* **GET /item/<int:item_id>:**
  * Obtém um item específico pelo ID.
* **GET /causar-erro:**
  * Simula um erro no servidor.
* **POST /processar-dados:**
  * Processa dados enviados no corpo da requisição.
* **POST /criar-item:**
  * Cria um novo item.

### GET /dados-seguros
* **Descrição:** Retorna dados seguros após autenticação.
* **Cabeçalhos:**
  * `Authorization`: Token de autenticação
* **Resposta:**
  * `200 OK`: Dados seguros em formato JSON
  * `401 Unauthorized`: Token inválido ou ausente

### GET /item/<int:item_id>
* **Descrição:** Obtém um item com base no ID fornecido.
* **Parâmetros:**
  * `item_id`: ID do item a ser obtido (inteiro)
* **Resposta:**
  * `200 OK`: Item encontrado em formato JSON
  * `404 Not Found`: Item com o ID fornecido não encontrado

### GET /causar-erro
* **Descrição:** Simula um erro no servidor para fins de teste.
* **Resposta:**
  * `500 Internal Server Error`: Mensagem de erro inesperado em formato JSON

### POST /processar-dados
* **Descrição:** Processa dados enviados no corpo da requisição.
* **Corpo da Requisição:**
  * JSON contendo uma chave `key`
* **Resposta:**
  * `200 OK`: Dados processados com sucesso em formato JSON
  * `400 Bad Request`: Chave ausente ou requisição inválida

### POST /criar-item
* **Descrição:** Cria um novo item.
* **Corpo da Requisição:**
  * JSON contendo o nome do item a ser criado (`name`)
* **Resposta:**
  * `201 Created`: Item criado com sucesso em formato JSON
  * `409 Conflict`: Item já existe
