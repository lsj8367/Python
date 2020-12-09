import pandas as pd
from konlpy.tag import Okt, Kkma
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from collections import Counter

okt = Okt()
word_dict = {}

def Word_Slicing(fileName):
    with open(fileName, mode = 'r') as f:
        lines = f.read().split('\n')
        lines = " ".join(lines)
        lines = re.sub(r'[\ta-zA-Z0-9-=+,#/\?:★^$.@*\"※~&%ㆍ!』◈\\‘|\(\)\[\]\<\>`\']',' ',lines)
        lines = lines.split()
        #print(lines)
        
    for line in lines:
        datas = okt.pos(line)
        #print(datas)
        for word in datas:
            if word[1] == 'Noun' and len(word[0]) >= 2:
                if not(word[0] in word_dict): # dict안에 word 단어가 없다면 0
                    word_dict[word[0]] = 0
                word_dict[word[0]] += 1 # 있으면 1씩 누적
        
    #rint(word_dict)
    
    keys = sorted(word_dict.items(), key = lambda x:x[1], reverse=True)
    #print(keys)
    df = pd.DataFrame([word_dict.keys(), word_dict.values()])
    df = df.T
    df.columns = ['단어', '빈도수']
    #print(df)
    df = df.sort_values(by=['빈도수'], axis = 0, ascending = False)
    
    df.to_excel(excel_writer = 'sample.xlsx')
    #print("저장됐음")

if __name__ == '__main__':
    Word_Slicing('jejudoMatJip.txt')
