# Este é o código do cliente.py

import websocket
import threading

# --- Funções que reagem a eventos do WebSocket ---

# Esta função será executada quando a conexão for aberta com sucesso
def on_open(ws):
    print("--- ✅ Conexão estabelecida com o servidor! ---")
    
    # Prepara e envia a primeira mensagem
    mensagem = "E aí, servidor! Sou o cliente, usando a filosofia Chyiara!"
    ws.send(mensagem)
    print(f">>> 📤 Mensagem enviada: {mensagem}")

# Esta função será executada toda vez que uma mensagem chegar do servidor
def on_message(ws, message):
    print(f"\n<<< 📥 Mensagem recebida do servidor: {message}")

# Esta função será executada se der algum erro na conexão
def on_error(ws, error):
    print(f"--- ❌ ERRO: {error} ---")

# Esta função será executada quando a conexão for fechada
def on_close(ws, close_status_code, close_msg):
    print("--- 🔌 Conexão fechada ---")


# --- Ponto de partida do programa ---
if __name__ == "__main__":
    # O endereço do nosso servidor local que está rodando
    # "ws" significa WebSocket, e "127.0.0.1" é um apelido para "este próprio computador"
    endereco_servidor = "ws://127.0.0.1:8000"
    
    print(f"🚀 Cliente Chyiara tentando se conectar a {endereco_servidor}...")
    
    # Cria a instância do cliente WebSocket, ligando cada evento (on_open, on_message)
    # à sua respectiva função que criamos acima.
    ws = websocket.WebSocketApp(endereco_servidor,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    # Roda o cliente para sempre, mantendo a conexão viva para poder receber mensagens.
    # Pressione Ctrl+C para fechar.
    ws.run_forever()
