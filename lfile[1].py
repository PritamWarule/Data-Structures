p=open('file.txt')
Lc=0
Wc=0
for i in p:
    Lc=Lc+1
    s=i.split()
    print("Words of line:- ",Lc)
    for x in s:
        Wc=Wc+1
        print("\n\t",x)
    print(f"\nLine {Lc} looks like : - {i}")
    #print(i)
print("\nTotal Line count:-",Lc)
print("\nTotal Word count:-",Wc)