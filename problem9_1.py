n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)    
#find the sum of square of a digit in a given number
n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r**2
   n=n//10
print(sum)    
#sum of even digits
n=1234
sum=0
while n>0:
    r=n%10
    if(r%2==0):
        sum+=r
    n=n//10
print(sum)    
#reverse number
n=123
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
ans=int(rev)
print(ans)
print(type(ans))    




