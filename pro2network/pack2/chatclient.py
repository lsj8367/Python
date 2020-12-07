'''
멀티 채팅을 위한 클라이언트
'''

import socket
import threading
import sys

def Handler(socket):
    while True:
        data = socket.recv(1024)
        if not data:continue # 데이터없으면 건너뜀
        print(data.decode('utf-8'))
        
# 파이썬은 표준출력의 경우 버퍼링이 됨
sys.stdout.flush() # 현재 buffer에 저장된 내용을 출력장치로 내보내고 buffer를 비움

name = input('채팅 아이디 입력 : ')
cs = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
cs.connect(('192.168.0.135', 5555))
cs.send(name.encode('utf-8')) # 인코딩하여 소켓단위로 서버에 넘김

th = threading.Thread(target=Handler, args = (cs,))
th.start()

while True:
    msg = input() # 채팅 메세지 입력
    sys.stdout.flush()
    if not msg: continue
    cs.send(msg.encode('utf-8'))
    
cs.close()
    