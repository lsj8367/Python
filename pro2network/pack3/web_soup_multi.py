# 멀티 프로세싱을 이용한 웹 스크래핑
import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool

def get_links():  # 특정사이트에 하이퍼링크를 가져오기
    data = requests.get('https://beomi.github.io/beomi.github.io_old/').text
    soup = bs(data, 'html.parser')
    #print(soup)
    my_titles = soup.select('h3 > a')  # css의 selector  #h3안의 a태그만 가져오기
    data = []
    for title in my_titles:
        data.append(title.get('href'))
    return data
        
def get_content(link):
    abc_link = 'https://beomi.github.io' + link
    data = requests.get(abc_link).text #사이트안의 문자들
    soup = bs(data, 'html.parser') # 링크와 속성
    # 가져온 데이터로 뭔가를.... 그러나 우리는 그저 소요시간이 궁금함
    print(soup.select('h1')[0].text) # 첫번째 h1 태그의 텍스트 읽어오기
    
    
    
       
    
if __name__ == '__main__':
    start_time = time.time()
    #print(get_links())
    '''
    for link in get_links():
        get_content(link)
    '''    
    pool = Pool(processes = 5) # 5개의 프로세스 사용
    pool.map(get_content, get_links()) # 함수와 인자값을 매핑하면서 처리
    
    
    
    print('-------%s 초---------'%(time.time() - start_time))
    
    
    
    
    
    
    
    
    
    