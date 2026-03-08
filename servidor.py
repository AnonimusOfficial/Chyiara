# Este é o código do servidor.py

import asyncio
from simple_websocket_server import WebSocketServer, WebSocket

# Esta classe vai cuidar de cada cliente que se conectar
class ServidorChyiara(WebSocket):
    
    # Função que é chamada quando um cliente se conecta
    async def connected(self):
        print(f'🤝  Novo cliente conectado: {self.address}')

    # Função que é chamada quando um cliente se desconecta
    async def closed(self):
        print(f'👋  Cliente desconectado: {self.address}')

    # Função que é chamada quando o servidor recebe uma mensagem
    async def handle(self):
        # "self.data" contém a mensagem que o cliente enviou
        mensagem_recebida = self.data
        print(f'📥  Recebido de {self.address}: {mensagem_recebida}')
        
        # Monta uma resposta
        resposta = f'Eco da Chyiara: "{mensagem_recebida}"'
        
        # Envia a resposta de volta para o cliente
        await self.send(resposta)
        print(f'📤  Enviado para {self.address}: {resposta}')

# --- Ponto de partida do programa ---
if __name__ == '__main__':
    # Define o endereço e a porta onde o servidor vai rodar
    # '0.0.0.0' significa que ele vai aceitar conexões de qualquer lugar
    # 8000 é a porta que vamos usar
    host = '0.0.0.0'
    porta = 8000

    print(f'🔥 Servidor Chyiara iniciando em {host}:{porta}')
    print('Pressione Ctrl+C para fechar.')

    # Cria e inicia o servidor
    server = WebSocketServer(host, porta, ServidorChyiara)
    server.serve_forever()

