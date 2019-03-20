import time

def DieDaiF(m):
    a = 0
    b = 1
    n = 0
    while b <= m:
        a += b
        a, b = b, a
        n += 1
    return n

start = time.clock()
answer = DieDaiF(2**31)
end = time.clock()
print(answer)
print(end-start)
