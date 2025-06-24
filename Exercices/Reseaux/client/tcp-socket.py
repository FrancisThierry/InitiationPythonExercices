import socket
import time
temperature = {"capteur1": 20, "capteur2": 22.5, "capteur3": 21.3}

for capteur, temp in temperature.items():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12345))
        message = f'{{"capteur": "{capteur}", "temperature": {temp}}}'
        # message = r"{'test': 'test'}"
        s.sendall(message.encode())
        data = s.recv(1024)
        time.sleep(1)  # Pause de 1 seconde entre les envois