import time

count1 = 0
count2 = 0

def MaxInt(m):
    a = 0
    b = 1
    n = 0
    while b <= m:
        a += b
        a, b = b, a
        n += 1
    return n

def MaxIntAndTime(m):
    start = time.clock()
    n = MaxInt(m)
    end = time.clock()
    return n, end-start

def DieDaiF(m):
    global count1
    a = 0
    b = 1
    n = 0
    while n < m:
        a += b
        a, b = b, a
        n += 1
        count1 += 1
    return a

def DieDaiCountAndTime(m):
    global count1
    start = time.clock()
    DieDaiF(m)
    end = time.clock()
    return count1, end-start

def DiGuiF(m):
    global count2
    count2 += 1
    if m == 0:
        return 0
    if m == 1:
        return 1
    return DiGuiF(m-1)+DiGuiF(m-2)

def DiGuiCountAndTime(m):
    global count2
    start = time.clock()
    DiGuiF(m)
    end = time.clock()
    return count2, end-start
