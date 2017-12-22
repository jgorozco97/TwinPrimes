# from __future__ import division
# Algorithm to get all twin primes up to n+2
# Proof of correctness of algorithm can be found at http://vixra.org/abs/1701.0618
import numpy as np
import sympy as sm
import time as tm
import matplotlib.pyplot as plt


def GenWheel(n):
    s = [2, 3, 5, 7]
    q = 1
    for i in s:
        q = q * i
    whl = []
    for i in range(1, q, 2):
        if sm.isprime(i):
            whl = np.append(whl, i)

    i = 0
    t = 0
    b = [[0, 0]]
    while t < n / 2:
        for r in whl:
            t = int(q * i + r)
            if sm.isprime(t):
                if sm.isprime(n - t) and t < n - t:
                    # Modified net line to show combinations at origin.
                    b = np.append(b, [[t, n - n / 2 - t]], axis=0)
        i = i + 1
    return b


def TwinP(n):
    a1 = np.ones([2, n], int)
    for i in xrange(0, n):
        a1[0, i] = i
        a1[1, i] = i + 2

    p = 2
    # k=2.0
    # k=fr.fraction(n,1)
    k = n
    while p ** 2 <= n:
        print("Array size: {0:2d} Calculated size {1:.2f}").format(a1.shape[1], k)
        print("Sieving: {}").format(p)
        # print("Calculated size:{0:4f} ").format(k)

        i = 0
        while i < a1.shape[1]:
            if (a1[0, i] % p == 0 and a1[0, i] != p) or (a1[1, i] % p == 0 and a1[1, i] != p):
                a1 = np.delete(a1, i, 1)
            else:
                i += 1

            if a1.shape[1] < 10:
                print a1, k

            if p != 2:
                k = float(k * (1 - 2 / p))
            else:
                k = float(k / 2)
            p = sm.nextprime(p)

    print("Final array:")
    print(a1)
    print(k)


# TwinP(8000)

def PrintArr(m):
    for i in range(0, m.shape[0]):
        print(m[i, 0], m[i, 1])
        if i % 10000 == 0 and False:
            print('Pause')
            tm.sleep(1)


def MainPlot():
    plt.axis([0, 250, 0, 250])
    ct = [[0, 0]]
    for x in range(10, 500, 2):
        arr = GenWheel(x)
        sa = [x, arr.shape[0]]
        ct = np.append(ct, [sa], axis=0)
        # PrintArr(arr)
    arr = np.transpose(arr)
    # print(arr)
    # plt.setp(marker, '.')
    # oth=np.arange(0,300,2)
    # fun=3*oth+2
    # plt.axis([0,x/2,0,n/2])
    # plt.setp(ms,1)
    #plt.show(block=True)
    #plt.interactive(False)

    plt.plot(arr[0], arr[1], 'c.')
    plt.title('Solutions of Goldbach pairs for n=500 (y-axis adjusted)')
    plt.show(block=True)

    ct = np.transpose(ct)
    plt.title('Goldbach comet')
    plt.plot(ct[0], ct[1], 'g.')
    plt.show(block=True)
    # plt.plot(oth,fun,'bs')


MainPlot()

# n=300
# arr=GenWheel(n)
# arr=np.transpose(arr)
# plt.plot(arr[0],arr[1],'b.')
# plt.show()

# print(arr)
