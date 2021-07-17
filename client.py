import socket, sys
ip = '192.168.56.1'
port=50000
address=(ip,port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(address)
except socket.error:
    print ("la connexion a échoué")
    sys.exit()
print ("connexion établie avec le serveur")
msgServeur = client.recv(1024).decode('utf-8')
while 1 : 
    if msgServeur.upper()== "FIN" or msgServeur=="":
        break
    print ("serveur> ",msgServeur)
    msgClient = input ("client>")
    client.send(msgClient.encode('utf-8'))
    msgServeur=client.recv(1024).decode('utf-8')
    
print("connexion interrompur.")
client.close()