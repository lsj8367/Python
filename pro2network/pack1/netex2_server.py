# 단발성 Echo Server
from socket import *

# socket
serverSock = socket(AF_INET, SOCK_STREAM) # 소켓의 종류, 유형 써줬음 객체 생성
serverSock.bind(('192.168.0.135', 9999)) # 0~ 1024 는 시스템에서 사용 8080 3306 1521 제외 binding
serverSock.listen(1) # 1 ~ 5 동시 최대 접속수

print('에코 서버 서비스 중....')


conn, addr = serverSock.accept() # 연결 대기
print('client addr : ', addr)
print('client conn : ', conn)

print('클라이언트로 부터 넘어온 정보 수신 결과 : ', conn.recv(1024).decode())

conn.close()
serverSock.close()
