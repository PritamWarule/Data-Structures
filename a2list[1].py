f=open('alist.txt')
for t in f:
    #t=t.strip()
    t=t.split()
    if t.startswith("From"):
        print(t[2])