import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket Criado com sucesso!!!')

host = 'localhost'
portal = 5433
mensagem = "Ola servidor blz ?"

try:
    print('Cliente:' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: " + dados)
finally:
    print('Cliente: Fechando a Conexão')
    s.close()
