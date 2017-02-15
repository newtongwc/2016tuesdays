def recurse(a):
    a.append(a[len(a)-1]+1)
    for x in a:
        print 1
        print x
    if a[len(a)-1]<8:
        recurse(a)
a = [2]
recurse(a)
