import pandas as pd
from konlpy.tag import Okt, Kkma
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from collections import Counter
okt = Okt()
with open('jejudoMatJip.txt', mode = 'r') as f:
    lines = f.read().split('\n')
    lines = " ".join(lines)
    lines = re.sub(r'[\ta-zA-Z0-9-=+,#/\?:★^$.@*\"※~&%ㆍ!』◈\\‘|\(\)\[\]\<\>`\']',' ',lines)
    lines = lines.split()
    print(lines)
def wordCloud():
    msg = " ".join(lines)
    nouns = okt.nouns(msg) # 명사만 추출
    result = [] # 두글자 이상의 단어만 담기위한 list 변수
    for imsi in nouns: 
        if len(imsi) > 1: # 두글자 이상의 것만 list에 넣기
            result.append(imsi)
    
    print(result)
    count = Counter(result) # 똑같은 단어 셈해주기
    print(count)
    
    tag = count.most_common(20) # 상위 50개의 명사만 작업에 참여
    
    import pytagcloud
    taglist = pytagcloud.make_tags(tag, maxsize = 100) # 태그를 생성, color 등등 설정을 안주면 빈도에따라서 색과 크기가 자동으로 나뉘게 됨
    print(taglist) # 한글 글꼴이 없으면 깨지기 때문에 글꼴 다운
    
    # tag_image 생성 후 저장
    # output = 이름 fontname은 json안에 Name값
    pytagcloud.create_tag_image(taglist, 'word.png', size = (900, 600), fontname = 'korean', rectangular = False) # word.png로 저장됨
    
    img = mpimg.imread('word.png') #이미지 로드
    plt.imshow(img)
    plt.show()


wordCloud()