from math import *

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        elif n == 1:
            print(1)
        else:
            dem = 0
            while n > 1:
                if n%2 == 0:
                    dem += 1
                    # print(n, end=' ')
                    n = n//2
                else:
                    dem += 1
                    # print(n, end = ' ')
                    n = n*3 + 1
            if n == 1:
                dem += 1
            print(dem)