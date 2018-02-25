import time
import os
import sys

def format_number(x):
    return str(x) if x > 9 else "0" + str(x)

def get_local_time():
    h = time.localtime().tm_hour
    m = time.localtime().tm_min
    s = time.localtime().tm_sec

    array = [h, m, s]

    display_numbers = [format_number(x) for x in array]

    return ":".join(display_numbers)


def main(argv):
    global h, m, s
    while 1:
        time.sleep(1)
        os.system("cls")
    
        ctime = get_local_time()

        print(ctime)


if __name__ == '__main__':
	main(sys.argv)