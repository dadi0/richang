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
    qsort(mylist, first, i-1)
    qsort(mylist, i+1, end)
