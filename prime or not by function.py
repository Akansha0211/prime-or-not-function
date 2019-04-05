def prime(li):
    count=0
    for i in (2,li):
        if li==2:
            return False #False for prime
        if li%i==0:
            count+=1
            return True  #True for not  prime
        else:
            return False  #False for prime
            
n=int(input("Enter the number of elements of a list"))
li=[]
for i in range (n):
    x=int(input())
    li.append(x)
    print(li)
a=list(map(prime,li))
print(a)
    
