'''
네트워크 : 네트워크에 필요한 구성 요소들을 일컫는 말(케이블, 라우터, 무선링크, 기타 장비..)
네트워킹 : 네트워크 데이터를 컴퓨터 간에 주고받는 과정 / 송수신.

socket : 네트워크를 위한 통신 채널 - TCP/IP 기반의 프로그래밍 인터페이스
'''
import socket

print(socket.getservbyname('http', 'tcp'))   #80 포트번호 www환경
print(socket.getservbyname('telnet', 'tcp')) #23 원격 컴 접속 시
print(socket.getservbyname('ftp', 'tcp'))    #21 파일 전송용
print(socket.getservbyname('pop3', 'tcp'))   #110 이메일 수신 시
print(socket.getservbyname('smtp', 'tcp'))   #25 메일 송수신

print(socket.getaddrinfo('www.naver.com', 80, proto = socket.SOL_TCP))


