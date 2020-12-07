'''
SimpleHTTPServer 구축 후 http 서비스 진행
- GET, HEAD처리는 가능
- POST, CGI 처리 불가능 클라이언트로부터 받은값 처리 X
'''
# HTTPServer : 기본적인 Socket 연결을 관리
# SimpleHTTPRequestHandler : 클라이언트 요청을 처리 get, head만 가능함

from http.server import SimpleHTTPRequestHandler, HTTPServer

port = 7777

handler = SimpleHTTPRequestHandler
serv = HTTPServer(('127.0.0.1', port), handler)
print('----웹 서비스 시작----')

serv.serve_forever() # 무한루프에 빠지게 만들음

