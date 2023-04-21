import socket
import time

IP_ADDRESS = input("Enter sign IP ADDRESS > ")
PORT = int(input("Enter a port number > "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((IP_ADDRESS, PORT))

steps = [
        (10000, b'\x01Z00\x02E$$$$\x04'),
       #(500, b'\x01Z00\x02Set play list to Flash\x04'),
        (500, b'SETPLAYLISTTOC'),
        (500, b'\x01Z00\x02E#DE\x04'),
        (500, b'\x01Z00\x02E.SLA\x04'),
        (500, b'\x01Z00\x02E#T1\x04'),
        (500, b'\x01Z00\x02E#MbOb\x04'),
        (500, b'\x01Z00\x02AATHIS SIGN IS NOW SETUP FOR ADP PROTOCOL\x04'),
]
        

for i in steps:
    data = i[1]
    print(f"sending {i}")
    s.sendall(data)
    time.sleep(i[0]/1000)

s.close()
