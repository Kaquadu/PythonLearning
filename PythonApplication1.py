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

    print_numbers(array)

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
    
    one = ["  #", " ##", "  #", "  #", "  #"]
    two = ["###", "  #", "###", "#  ", "###"]
    thr = ["###", "  #", "###", "  #", "###"]
    fou = ["#  ", "# #", "###", "  #", "  #"]
    fiv = ["###", "#  ", "###", "  #", "###"]
    six = ["###", "#  ", "###", "# #", "###"]
    sev = ["###", "  #", "  #", "  #", "  #"]
    eig = ["###", "# #", "###", "# #", "###"]
    nin = ["###", "# #", "###", "  #", "###"]
    nul = ["###", "# #", "# #", "# #", "###"]
    numb = [nul, one, two, thr, fou, fiv, six, sev, eig, nin]

    toPrint = ["", "", "", "", ""]

    for i in range(5):
        for x in range(10):
            if (arrayInts[0] == x):
                toPrint[i] += numb[x][i]
                toPrint[i] += " "
        for x in range(10):
            if (arrayInts[1] == x):
                toPrint[i] += numb[x][i]
                toPrint[i] += "   "
        for x in range(10):
            if (arrayInts[2] == x):
                toPrint[i] += numb[x][i]
                toPrint[i] += " "
        for x in range(10):
            if (arrayInts[3] == x):
                toPrint[i] += numb[x][i]
                toPrint[i] += "   "
        for x in range(10):
            if (arrayInts[4] == x):
                toPrint[i] += numb[x][i]
                toPrint[i] += " "
        for x in range(10):
            if (arrayInts[5] == x):
                toPrint[i] += numb[x][i]

    for i in range(0, 5):
        print (toPrint[i])
    

def main(argv):
    while 1:
        time.sleep(1)
        os.system("cls")
    
        get_local_time()

        #print(ctime)

if __name__ == '__main__':
	main(sys.argv)