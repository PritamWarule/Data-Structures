f=open('alist.txt')
for t in f:
    t=t.strip()
    fsp=t.find('net')
    ssp=t.find(' ',fsp)
    #print(ssp)
    #print(fsp)
    print(t[39:42])
    #print(t)
    