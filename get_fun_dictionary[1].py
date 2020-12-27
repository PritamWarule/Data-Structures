pritam={}
line=input("Enter line> ")
line=line.split()
for word in line:
    pritam[word]=pritam.get(word,0)+1
print("Count",pritam)