import time

def delayMicrosecond(t):
    start,end = 0,0
    start = time.time()
    t = (t-1000)/1000000
    while end-start < t:
        end = time.time()

if __name__ == '__main__':
    t = time.time()
    print (str(int(round(t * 1000))))
    delayMicrosecond(1000)
    t = time.time()
    print (str(int(round(t * 1000))))
    #do some change
