# CGIHTTPRequestHandler 구축 후 http 서비스 진행
# - GET, HEAD, POST, CGI 모두 다 가능하다.
# - CGI - 웹서버와 외부 프로그램 사이에서 서로간의 정보를 주고받는 방법이나 규약. 이로 인하여 대화형 웹 페이지가 구현가능하다.
#       - 클라이언트가 요청한 db 자료 처리 후 출력
#       - form을 사용한 자료 전송, 메일 전송
from http.server import CGIHTTPRequestHandler, HTTPServer

port = 8888

class HandlerClass(CGIHTTPRequestHandler):
    cg_directories = ['/cgi_bin'] # ('/cgi_bin')도 가능 dict, list 가능

serv = HTTPServer(('127.0.0.1', port), HandlerClass)
print('----웹 서비스 시작----')

serv.serve_forever()