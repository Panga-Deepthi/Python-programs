
n1=int(input("enter:"))
n2=int(input("enter:"))
if n1>n2:
    greater=n1
else:
    greater=n2
while True:
    if greater%n1==0 and greater%n2==0:
        lcm=greater
        break
    greater+=1
print(greater)






