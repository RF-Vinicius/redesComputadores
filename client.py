import socket
port = 12000
ipv4 = "192.168.10.171"
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM sinaliza que estaremos usando o protocolo UDP

while True:
    mensagem_envio = input('Digite aq: ')
    
    cliente.sendto(mensagem_envio.encode(), (ipv4, port)) #Transforma para byte a mensagem que vem como string e manda via UDP
    mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(2048) # Recebe o tamanho da palavra
    print(mensagem_bytes.decode())
    