# Thread의 자원공유, 활성화/비활성화 wait(), notify()
import threading, time

bread_plate = 0 # 빵접시 : 10

lock = threading.Condition() # Lock을 위한 조건을 갖춤

class Maker(threading.Thread): # 빵 생산자
    def run(self):
        global bread_plate
        for i in range(30):
            lock.acquire()
            while bread_plate >= 10:
                print("빵 생산 초과로 대기")
                lock.wait() # Thread 비활성화
            bread_plate += 1
            print('빵 생산 : ', bread_plate)
            lock.notify() # 스레드 활성화
            lock.release()
            time.sleep(0.05)
                
                

class Consumer(threading.Thread): #  빵 소비자
    def run(self):
        global bread_plate
        for i in range(30):
            lock.acquire()
            while bread_plate < 1:
                print("빵 없어서 기다림")
                lock.wait()
            bread_plate -= 1
            print('빵 소비 후 : ', bread_plate)
            lock.notify()
            lock.release()
            time.sleep(0.06)

mak = []; con = []

for i in range(5):
    mak.append(Maker())
for i in range(5):
    con.append(Consumer())

for th1 in mak:
    th1.start()
    
for th2 in con:
    th2.start()   
     
for th1 in mak:
    th1.join()
    
for th2 in con:
    th2.join()
    
print("오늘 영업 끝!!!")    
    
    
    
    
    