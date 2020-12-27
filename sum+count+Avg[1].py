count=0
sum=0
while True:
    n=input("Enter next no> ")
    if n=='exit':
        break
    try :
        n=float(n)
    except:
            print("Entered bad data")
            continue
    sum=sum+n
    count=count+1
print(f"Sum:{sum} count:{count} Average:{sum/count}")    