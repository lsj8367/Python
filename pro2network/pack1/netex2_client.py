# client로 server에 접속
from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.168.0.135', 9999)) # 능동적으로 server에 접속을 시도

# packet(header + body로 구성) 단위로 전송 - sequential한  binary data 형태로 전송한다.
clientSock.sendall('안녕 반가워 lsj'.encode(encoding='utf_8', errors = 'strict'))
clientSock.close()



