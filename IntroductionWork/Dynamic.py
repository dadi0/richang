def dynamic(a):
    b = []   #结果
    length = len(a)
    for i in range(length):
        c = []
        sum1 = 0
        for j in range(i):
            c.append(sum1)
        for j in range(i, length):
            sum1 += a[j]
            c.append(sum1)
        b.append(c)
    for i in range(length-1):  #求每位最大序列和
        for j in range(i+1, length):
            b[i][j] = max(b[i][j], b[i][j-1])
    d = [b[0][0]]  #0--i-1最大序列和
    e = [b[-1][-1]]  #i--n-1最大序列和
    for j in range(1, length):
        key = b[0][j]
        for i in range(1, j+1):
            if key < b[i][j]:
                key = b[i][j]
        d.append(key)
    for j in range(1, length):
        key = b[-1][-1]
        for i in range(-j-1, -1):
            if key < b[i][-1]:
                key = b[i][-1]
        e.append(key)
    ans = [e[-1]]  #n个元素从左到右的分界线为下标
    for i in range(1, length):
        ans.append(d[i-1]+e[-i-1])
    ans.append(d[-1])
    key = ans[0]
    for i in range(1, length+1):
        if key < ans[i]:
            key = ans[i]
    return key
