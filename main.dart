import 'dart:io';

void main() async {
  Socket socket = await Socket.connect('adresse_ip_serveur', 12345);
  
  // Envoyer des données au serveur
  socket.write('Données à envoyer au serveur');

  // Écouter les données du serveur
  socket.listen((List<int> data) {
    print('Données reçues du serveur: ${String.fromCharCodes(data)}');
  });

  // Fermer la connexion
  //socket.close();
}
