f=open("file.txt")
p=f.read()
print(len(p))
print(p)
print(p[:59])
if "hari" in p:
    print("yeesss")
else:
    print("nooo")