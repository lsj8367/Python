import pandas as pd
from konlpy.tag import Okt, Kkma
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from collections import Counter
import unicodedata # 인스타 자/모음 분리현상 제거하기 위한 라이브러리

okt = Okt()
word_dict = {}

# travel = pd.read_csv('travel.csv')
# #lines = unicodedata.normalize('NFC', lines)
list = []

def Word_Slicing(fileName):
    with open(fileName, mode = 'r', encoding = 'utf-8') as f: # , encoding = 'utf-8'
        lines = f.read().split('\n')
        print(type(lines))
        for txt in lines:
            txt = unicodedata.normalize('NFC', txt)            
            txt = txt.split('\n')
            #print(type(txt))
            list.append(txt)
            data = pd.DataFrame(list) # 서울에 사시느ㄴ  식의 깨짐현상 제거
        print(data)
        data[0] = data[0].str.replace(pat=r'[^가-힣]', repl=r' ', regex=True)
        print(data)
    data[0].to_csv('test.csv', encoding='utf8', index = False)
    print('저장완료') # 단어 임베딩용 엑셀파일


    for line in data[0]:
        datas = okt.pos(line)
        #print(datas)
        for word in datas:
            if word[1] == 'Noun' and len(word[0]) >= 2:
                if not(word[0] in word_dict): # dict안에 word 단어가 없다면 0
                    word_dict[word[0]] = 0
                word_dict[word[0]] += 1 # 있으면 1씩 누적
        
    
    #print(word_dict)
    
    keys = sorted(word_dict.items(), key = lambda x:x[1], reverse=True)
    #print(keys)
    df = pd.DataFrame([word_dict.keys(), word_dict.values()])
    df = df.T
    df.columns = ['단어', '빈도수']
    df = df.sort_values(by=['빈도수'], axis = 0, ascending = False)
    #print(df)
    
#     df.to_excel(excel_writer = '{}(word).xlsx'.format(fileName[0:-4]))
#     print("저장됐음")

if __name__ == '__main__':
    Word_Slicing('travel.csv')

