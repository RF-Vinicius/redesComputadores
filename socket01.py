import socket
port = 12000
ipv4 = ""
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM sinaliza que estaremos usando o protocolo UDP
servidor.bind(('', 12000))

while True:
    mensagem_bytes, endereco_ip_client = servidor.recvfrom(2048) # Recebe o tamanho da palavra
    mensagem_resposta = mensagem_bytes.decode().upper()
    servidor.sendto(mensagem_resposta.encode(), endereco_ip_client)
    
    print(mensagem_resposta)