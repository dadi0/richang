def qsort(mylist, first, end):
    if first >= end:
        return
    i, j = first, end
    key = mylist[i]
    while i < j:
        while key <= mylist[j] and i < j:
            j -= 1
        mylist[i] = mylist[j]
        while key >= mylist[i] and i < j:
            i += 1
        mylist[j] = mylist[i]
    mylist[i] = key
    print(i)
    print(mylist)
    qsort(mylist, first, i-1)
    qsort(mylist, i+1, end)

a = '10 8 6 4 3 5 7 9 6'.split()
qsort(a, 0, 8)
print(a)
