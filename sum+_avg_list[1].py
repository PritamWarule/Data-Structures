p=[ ]
while True:
    t=input("enter number and done at last: ")
    if t=='done':
        break
    t=float(t)
    p.append(t)
avg=sum(p)/len(p)
print("Average",avg)