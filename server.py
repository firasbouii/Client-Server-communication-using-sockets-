import socket, sys
# 1) création de la socket : 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ip = socket.gethostbyname(socket.gethostname())
ip='192.168.56.1'
port = 50000
counter=0
address = (ip,port)
# 2) liaison du socket à une adresse précise :
try:
     server.bind(address)
except socket.error:
     print("La liaison du socket à l'adresse choisie a échoué.")
     sys.exit()
while 1:
#  3) Attente de la requête de connexion d'un client :
     print("Serveur prêt, en attente de requêtes ...")
     server.listen(2)
# 4) Etablissement de la connexion :
     connexion, addr = server.accept()
     counter +=1
     print("Client connecté, adresse IP %s, port %s" % (addr[0], addr[1]))

# 5) Dialogue avec le client :
     msgServeur ="Vous êtes bien connecté au serveur . Envoyez vos messages."
     connexion.send(msgServeur.encode("Utf8"))
     msgClient = connexion.recv(1024).decode("Utf8")
     while 1:
      print("Client>", msgClient)
      if msgClient.upper() == "FIN" or msgClient =="":
              break
      msgServeur = input("Serveur> ")
      connexion.send(msgServeur.encode("Utf8"))
      msgClient = connexion.recv(1024).decode("Utf8")

 # 6) Fermeture de la connexion :
     connexion.send("fin".encode("Utf8"))
     print("Connexion interrompue.")
     connexion.close()

     ch = input("<R>ecommencer <T>erminer ? ")
     if ch.upper() =='T':
       break
