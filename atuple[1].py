t=input("Enter file name> ")
d={}
s=open(t)
s=s.read()
p=s.split()
for word in p:
    d[word]=d.get(word,0)+1
print(d)
l=[]
for k,v in d.items():
    l.append((v,k))
l=sorted(l,reverse=True)
print(l)
#print(dict(l))
#print(ft)
#for k,v in ft.items():
    #print(k,v)