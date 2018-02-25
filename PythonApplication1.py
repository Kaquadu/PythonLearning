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

    print_numbers(display_numbers)

    #return ":".join(display_numbers)
    


def print_numbers(array):
    arrayInts = []
    arrayStr = []

    #print(array)

    for x in array:
        arrayStr += str(x)

    for x in arrayStr:
        arrayInts.append(int(x))

    #print(arrayStr)
    
    NRS_DICT = {
    1 : ["  #", " ##", "  #", "  #", "  #"],
    2 : ["###", "  #", "###", "#  ", "###"],
    3 : ["###", "  #", "###", "  #", "###"],
    4 : ["#  ", "# #", "###", "  #", "  #"],
    5 : ["###", "#  ", "###", "  #", "###"],
    6 : ["###", "#  ", "###", "# #", "###"],
    7 : ["###", "  #", "  #", "  #", "  #"],
    8 : ["###", "# #", "###", "# #", "###"],
    9 : ["###", "# #", "###", "  #", "###"],
    0 : ["###", "# #", "# #", "# #", "###"]
    }

    number_strings = [NRS_DICT[x] for x in arrayInts]
    for row_num in range(5):
        row = [x[row_num] for x in number_strings]
        print (' '.join(row))
    

def main(argv):
    while 1:
        time.sleep(1)
        os.system("cls")
    
        get_local_time()

        #print(ctime)

if __name__ == '__main__':
	main(sys.argv)