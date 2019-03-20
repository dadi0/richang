import time

count = 0

def DiGuiF(n):
    global count
    count += 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return DiGuiF(n-1)+DiGuiF(n-2)

start = time.clock()
DiGuiF(35)
end = time.clock()
print(end-start)
print(count)
