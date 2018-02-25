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

    write_local_time(array)

    return ":".join(display_numbers)

def write_local_time(arr):
    if arr[0] <= 9:
        if arr[1] <= 9:
            if arr[2] <= 9:
                print_time(0, arr[0], 0, arr[1], 0, arr[2])
            else:
                print_time(0, arr[0], 0, arr[1], str(arr[2])[0], str(arr[2])[1])
        else:
            if arr[2] <= 9:
                print_time(0, arr[0], str(arr[1])[0], str(arr[1])[1], 0, arr[2])
            else:
                print_time(0, arr[0], str(arr[1])[0], str(arr[1])[1], str(arr[2])[0], str(arr[2])[1])
    else:
        if arr[1] <= 9:
            if arr[2] <= 9:
                print_time(str(arr[0])[0], str(arr[0])[1], 0, arr[1], 0, arr[2])
            else:
                print_time(str(arr[0])[0], str(arr[0])[1], 0, arr[1], str(arr[2])[0], str(arr[2])[1])
        else:
            if arr[2] <= 9:
                print_time(str(arr[0])[0], str(arr[0])[1], str(arr[1])[0], str(arr[1])[1], 0, arr[2])
            else:
                print_time(str(arr[0])[0], str(arr[0])[1], str(arr[1])[0], str(arr[1])[1], str(arr[2])[0], str(arr[2])[1])

def print_time(num1, num2, num3, num4, num5, num6):
    arrayInts = []
    arrayMixed = [num1, num2, num3, num4, num5, num6]
    for x in arrayMixed:
        arrayInts.append(int(x))
    
    one = ["  #", " ##", "  #", "  #", "  #"]
    two = ["###", "  #", "###", "#  ", "###"]
    thr = ["###", "  #", "###", "  #", "###"]
    fou = ["#  ", "#  ", "###", "  #", "  #"]
    fiv = ["###", "#  ", "###", "  #", "###"]
    six = ["###", "#  ", "###", "# #", "###"]
    sev = ["###", "  #", "  #", "  #", "  #"]
    eig = ["###", "# #", "###", "# #", "###"]
    nin = ["###", "# #", "###", "  #", "###"]
    nul = ["###", "# #", "# #", "# #", "###"]
    numb = [nul, one, two, thr, fou, fiv, six, sev, eig, nin]

    toPrint = ["", "", "", "", ""]

    for i in range(5):
        for x in range(9):
            if (arrayInts[0] == x):
                toPrint[i] += numb[x][i]
                toPrint[i] += " "
        for x in range(9):
            if (arrayInts[1] == x):
                toPrint[i] += numb[x][i]
                toPrint[i] += " "
        for x in range(9):
            if (arrayInts[2] == x):
                toPrint[i] += numb[x][i]
                toPrint[i] += " "
        for x in range(9):
            if (arrayInts[3] == x):
                toPrint[i] += numb[x][i]
                toPrint[i] += " "
        for x in range(9):
            if (arrayInts[4] == x):
                toPrint[i] += numb[x][i]
                toPrint[i] += " "
        for x in range(9):
            if (arrayInts[5] == x):
                toPrint[i] += numb[x][i]
                toPrint[i] += " "

    for i in range(0, 5):
        print (toPrint[i])
    

def main(argv):
    while 1:
        time.sleep(1)
        os.system("cls")
    
        ctime = get_local_time()

        print(ctime)

if __name__ == '__main__':
	main(sys.argv)