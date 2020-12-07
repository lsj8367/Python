import socket
import sys

#HOST = '192.168.0.135'
HOST = '' # 현재 수행중인 컴퓨터의 ip를 자동으로 인지. 동적
PORT = 7788

# socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serverSock.bind((HOST, PORT)) # 0~ 1024 는 시스템에서 사용 8080 3306 1521 제외 binding
    serverSock.listen(5) # 1 ~ 5 동시 최대 접속수
    print('server start')
    
    while True:
        conn, addr = serverSock.accept()
        print('client info : ', addr[0], addr[1]) # ip, port
        print('수신정보 : ', conn.recv(1024).decode()) # 직렬로 들어오는것을 해석
        
        # 서버가 클라이언트에게 자료를 전송
        conn.send(('from server : ' + str(addr[1]) + ' 행복해~').encode('utf_8'))
        
        
except socket.error as err:
    print('err : ', err)
    sys.exit()
finally:
    serverSock.close()
