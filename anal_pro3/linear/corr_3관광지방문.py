# data.co.kr에서 관광지자료를 읽음
# 국내 관광지에 대해 미국인, 일본인, 중국인 관광객 출입 데이터로 상관관계 분석
import json
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')
import pandas as pd
import numpy as np

def setScatterChart(tour_table, all_table, tourpoint):
    # 계산할 관광지명에 해당하는 자료만 뽑아 tour 변수에 저장하고 외국인 관광객 자료와 병합
    tour = tour_table[tour_table['resNm'] == tourpoint] # 관광지들중 정해놓은 5개 tour_table 추출
    merge_table = pd.merge(tour, all_table, left_index = True, right_index = True) #년도별로 미국,일본,중국 관광객수 병합
    #print(merge_table)
    
    # 시각화
    fig = plt.figure()
    fig.suptitle(tourpoint + '상관관계 분석')
    
    plt.subplot(1, 3, 1)
    plt.xlabel('중국인 입장수')
    plt.ylabel('외국인 입장인원 수')
    lamb1 = lambda p:merge_table['china'].corr(merge_table['ForNum']) # 중국인 입국수와 외국인관광객 수의 상관계수
    r1 = lamb1(merge_table)
    print("r1 :", r1)
    plt.title('r={:.5f}'.format(r1))
    plt.scatter(merge_table['china'], merge_table['ForNum'], alpha = 0.8, s = 6, c = 'black')
    
    plt.subplot(1, 3, 2)
    plt.xlabel('일본인 입장수')
    plt.ylabel('외국인 입장인원 수')
    lamb2 = lambda p:merge_table.japan.corr(merge_table['ForNum']) # 일본인 입국수와 외국인관광객 수의 상관계수
    r2 = lamb2(merge_table)
    print("r2 :", r2)
    plt.title('r={:.5f}'.format(r2))
    plt.scatter(merge_table['japan'], merge_table['ForNum'], alpha = 0.8, s = 6, c = 'red') # 점의크기 s
    
    plt.subplot(1, 3, 3)
    plt.xlabel('미국인 입장수')
    plt.ylabel('외국인 입장인원 수')
    lamb3 = lambda p:merge_table.usa.corr(merge_table['ForNum']) # 일본인 입국수와 외국인관광객 수의 상관계수
    r3 = lamb3(merge_table)
    print("r3 :", r3)
    plt.title('r={:.5f}'.format(r3))
    plt.scatter(merge_table['usa'], merge_table['ForNum'], alpha = 0.8, s = 6, c = 'blue') # 점의크기 s
    plt.tight_layout() # 차트 간격 설정
    
    plt.show()
    return [tourpoint, r1, r2, r3]
    
    
def Gogo():
    # 서울시 관광지 정보 파일을 읽음
    fname = '서울특별시_관광지.json'
    jsonTp = json.loads(open(fname, 'r', encoding = 'utf-8').read()) # 디코딩하는것 str -> dict
    # print(jsonTp) # [{'ForNum': 14137, 'NatNum': 43677, 'addrCd': 1111, 'gungu': '종로구',
    tour_table = pd.DataFrame(jsonTp, columns=('yyyymm', 'resNm', 'ForNum')) # 년원일, 관광지명, 입장객수만 읽어오기
    tour_table = tour_table.set_index('yyyymm') # 연도순 정렬
    #print(tour_table)
    
    resNm = tour_table.resNm.unique()
    #print('관광지명 :', resNm)
    print('관광지명 :', resNm[:5]) # 5개만 보기 ['창덕궁' '운현궁' '경복궁' '창경궁' '종묘'] 만 작업에 참여
    
    # 중국인 관광지 정보파일 읽기
    cdf = '중국인방문객.json'
    jdata = json.loads(open(cdf, 'r', encoding = 'utf-8').read()) # json파일 읽어오기
    china_table = pd.DataFrame(jdata, columns = ('yyyymm', 'visit_cnt')) # yyyymm, visit_cnt만 보기
    china_table = china_table.rename(columns = {'visit_cnt': 'china'}) # 칼럼 visit_cnt를 china로 바꿈
    china_table = china_table.set_index('yyyymm') # 연도순 정렬
    #print(china_table)
    
    # 일본인 관광지 정보파일 읽기
    jdf = '일본인방문객.json'
    jdata = json.loads(open(jdf, 'r', encoding = 'utf-8').read()) # json파일 읽어오기
    japan_table = pd.DataFrame(jdata, columns = ('yyyymm', 'visit_cnt')) # yyyymm, visit_cnt만 보기
    japan_table = japan_table.rename(columns = {'visit_cnt': 'japan'}) # 칼럼 visit_cnt를 japan로 바꿈
    japan_table = japan_table.set_index('yyyymm') # 행번호를 년도로
    #print(japan_table)
    
    
    # 미국인 관광지 정보파일 읽기
    udf = '미국인방문객.json'
    jdata = json.loads(open(udf, 'r', encoding = 'utf-8').read()) # json파일 읽어오기
    usa_table = pd.DataFrame(jdata, columns = ('yyyymm', 'visit_cnt')) # yyyymm, visit_cnt만 보기
    usa_table = usa_table.rename(columns = {'visit_cnt': 'usa'}) # 칼럼 visit_cnt를 usa로 바꿈
    usa_table = usa_table.set_index('yyyymm') # 행 기준을 년도
    #print(usa_table)
    
    all_table = pd.merge(china_table, japan_table, left_index = True, right_index = True) # 두개씩밖에 못합침
    all_table = pd.merge(all_table, usa_table, left_index = True, right_index = True)
    #print(all_table, ' ', all_table.shape) # (72, 3)
    
    r_list = []
    for tourpoint in resNm[:5]:
        #print(tourpoint)
        r_list.append(setScatterChart(tour_table, all_table, tourpoint)) # 관광지명과 상관계수를 리스트에 넣어줌
    
    r_df = pd.DataFrame(r_list, columns = ('고궁명', '중국', '일본', '미국'))
    r_df = r_df.set_index('고궁명') # 인덱스를 고궁명으로 바꿈
    print(r_df)
    r_df.plot(kind = 'bar', rot = 50) # 글자방향돌림
    plt.show()
    
if __name__ == "__main__":
    Gogo()
    