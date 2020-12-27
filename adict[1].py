d={}
t=open('Dictass.txt')
t=t.read()
large=-1
#t=input(" ")
t=t.split()
#print(t)
for word in t:
    d[word]=d.get(word,0)+1
#print(d)
for k,v in d.items():
    print(k,v)
for k in d.keys():
             if d[k]>large:
                 large=d[k]
                 print("Done:Larger count word is :-",k,d[k])
     
