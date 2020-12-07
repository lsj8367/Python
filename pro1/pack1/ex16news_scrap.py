'''
news site 자료 스크랩핑 모듈 경험하기
'''
from newspaper import Article


#크롤링할 url 주소 입력

url = 'http://www.huffingtonpost.kr/taekyung-lee/story_b_18753362.html'

#언어가 한국어이므로 language='ko'로 설정

a = Article(url, language='ko')

a.download()

a.parse()

#기사 제목 가져오기

print('제목 : ', a.title)

print()

#기사 내용 가져오기(150자)

print('본문내용 : ', a.text)