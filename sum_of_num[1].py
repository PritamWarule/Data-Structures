large=-1
sum=0
c=0
a=[2,5,3,1,4]
for i in a:
    c=c+1
    sum=sum+i
    if i>large:
        large=i
print(f"*Large number till the end: {large} \n\t *Total sum of numbers are {sum}\n\t\t *Average of the all number is {sum/c}")