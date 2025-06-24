from client.client_reseau_tcp import ClientReseauTCP


client = ClientReseauTCP(host='localhost', port=12345)
message = '{"type": "test", "content": "Hello, World!"}'
client.envoyer(message)