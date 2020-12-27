f=open("file.txt")
for t in f:
    t=t.rstrip()
    if t.startswith ("Subject: "):
        continue
    print(t)