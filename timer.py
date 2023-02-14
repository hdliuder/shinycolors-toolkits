import time

def delay(t):
    start,end = 0,0
    start = time.time()
    while end-start < t:
        end = time.time()

if __name__ == '__main__':
    t = time.time()
    print (str(int(round(t * 1000))))
    delayMicrosecond(1000)
    t = time.time()
    print (str(int(round(t * 1000))))
    #do some change
