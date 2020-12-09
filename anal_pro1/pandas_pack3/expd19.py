# 한글 형태소 분석
# 말뭉치(corpus) : 자연어 연구를 위해 특정한 목적을 가지고 언어의 표본을 추출한 집합체
from konlpy.tag import Kkma, Okt, Komoran, Hannanum

kkma = Kkma() # Okt(), Komoran(),... 가능
print(kkma.sentences('여러분 만나서 반가워요. 잘 지내시나요'))
ss = """
각 지자체가 시설 방역수칙 준수 여부를 점검하면서 마스크 착용을 확인하게 된다. 잠깐 벗고 있다 적발되더라도 바로 과태료를 내야 하는 것은 아니다. 먼저 마스크 착용을 지도하고 따르지 않았을 때 과태료 10만원이 부과된다.
"""
print(kkma.sentences(ss))  # 문장
print(kkma.nouns(ss)) # 명사
print(kkma.pos(ss)) # 품사 태깅

print()
okt = Okt()
print(okt.nouns(ss))
print(okt.pos(ss))
print(okt.pos(ss, stem=True)) # 그래요 => 그렇다 표준형으로 변환해줌
print(okt.morphs(ss))