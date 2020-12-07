'''
thread로 날짜 및 시간 출력
'''
import time

now = time.localtime()
print("오늘 요일 %d"%(now.tm_wday)) # 월요일이 0 ~
print("오늘은 1년중 몇번째 날인가? %d"%(now.tm_yday)) # 1/1이 1값


import threading
def calendar_show():
    now = time.localtime()
    print("현재는 {}년 {}월 {}일 \n{}시 {}분 {}초".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    
def myRun():
    while True:
        now2 = time.localtime()
        if now2.tm_min == 41:break
        calendar_show()
        time.sleep(1)

th = threading.Thread(target=myRun)
th.start()

th.join()
print("프로그램 종료")
    