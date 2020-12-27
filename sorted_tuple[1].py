d={'a':1,'s':30,'c':26}
p=[ ]
print(sorted(d))
for k,v in d.items():
    p.append((v,k))
z=sorted(p,reverse=True)

print(p)
print(z)
print(sorted([(v,k) for k,v in d.items()], reverse=True))