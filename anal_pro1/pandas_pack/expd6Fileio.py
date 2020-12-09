# pandas로 파일 읽기
import pandas as pd

#df = pd.read_csv('testdata/ex1.csv')
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/ex1.csv') # url로 csv파일 가져올때
print(df, ' ', type(df))
print()
df = pd.read_table('testdata/ex1.csv', sep=',', skipinitialspace = True) # csv를 텍스트형태로 구분자 , 데이터앞 공백제거 skipinitialspace
print(df, ' ', type(df))
print()

df = pd.read_csv('testdata/ex2.csv', header = None) # 칼럼명 X, 헤더 없는 설정
print(df)
print()

df = pd.read_csv('testdata/ex2.csv', header = None, names = ['a','b']) # 칼럼명 X, 헤더 없는 설정, 뒤에서부터 칼럼명을 매핑해줌
print(df)

print()
df = pd.read_csv('testdata/ex2.csv', header = None, names = ['a','b','c','d','e']) # 칼럼명 X, 헤더 없는 설정, 뒤에서부터 칼럼명을 매핑해줌
print(df)

print() # 임의의 칼럼명을 index로 쓰고싶은 경우
df = pd.read_csv('testdata/ex2.csv', header = None, names = ['a','b','c','d','msg'], index_col = 'msg') # 칼럼명 X, 헤더 없는 설정, 뒤에서부터 칼럼명을 매핑해줌
print(df)

print() # 정규표현식 사용 \s 공백 뒤에 +는 1개이상
df = pd.read_table('testdata/ex3.txt', sep='\s+')
print(df)
print()
df = pd.read_table('testdata/ex3.txt', sep='\s+', skiprows = [1,3]) # skiprows 특정행 제외
print(df)

print()
df = pd.read_fwf('testdata/data_fwt.txt', widths=(10,3,5), names=('date','name','price'), encoding='utf8')
print(df)
print(df['date']) # 칼럼은 이렇게읽는다.
print(df.iloc[:3, 2])

# chunk 단위로 데이터 읽기 : 많은양의 자료를 원하는 크기만큼 할당/해제 하는 기능을 할 수 있다.
test = pd.read_csv('testdata/data_csv2.csv', header = None, chunksize = 3) # TextParser 객체 반환
#print(test)

for piece in test:
    #print(piece)
    print(piece.sort_values(by=2, ascending=True)) # 3번째열 기준 오름차순 정렬
    print()
