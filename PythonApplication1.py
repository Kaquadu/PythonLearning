import time,os,sys

def get_local_time():
    h = time.localtime().tm_hour
    m = time.localtime().tm_min
    s = time.localtime().tm_sec

    if h>9:
        hour = str(h)
    else:
        hour = "0" + str(h)

    if m>9:
        min = str(m)
    else:
        min = "0" + str(m)

    if s>9:
        sec = str(s)
    else:
        sec = "0" + str(s)

    return hour + ":" + min + ":" + sec




while 1:
    time.sleep(1)
    os.system("cls")
    
    ctime = get_local_time()

    print(ctime)