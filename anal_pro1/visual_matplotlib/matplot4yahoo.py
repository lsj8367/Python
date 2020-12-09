# pickle로 저장된 코스닥/ 코스피  종목코드로 yahoo가 지원하는 주식 자료 읽어 시각화
import pandas as pd
# pip install pandas_datareader
from pandas_datareader import data
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic') # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False # 음수 부호 깨짐 방지

kosdaq = pd.read_pickle('kosdaq.pickle')
kospi = pd.read_pickle('kospi.pickle')
print(kosdaq.head(3)) # 제일홀딩스  003380 이거 읽을거 종목코드
print(kospi.head(3)) # 넷마블게임즈  251270 이거 읽을거 종목코드

# yahoo가 지원하는 주식 자료 읽기
start_date = '2018-01-01'
tickers = ['003380.KQ', '251270.KS'] # 종목코드 주입
holding_df = data.get_data_yahoo(tickers[0], start_date)
net_df = data.get_data_yahoo(tickers[1], start_date)
print(holding_df.head(3))
print(net_df.head(3))

# 읽은자료 파일로 저장하기
# holding_df.to_csv('holding.csv')
# net_df.to_csv('net.csv')
# net_df.to_pickle('net.pickle')
# net_df.to_excel('net.xlsx', sheet_name = 'Sheet1')

# 파일 읽기
with open('net.csv', 'r') as f:
    print(f.read())
    
# 시각화
plt.plot(net_df)
plt.show()



