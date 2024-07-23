#arr=list(map(int,input().split()))
#peak=0
#for i in range(1,len(arr)-1):
#    if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
#        print(arr[i],end=" ") 
#if(arr[-1]>arr[-2] and arr[-1].peak):
#    peak=len(arr)-1
#print(arr[peak])
#sort the elements of first half is ascending and second half is descending
#gcd of 2 numbers
#euclidean algorithm
#a=int(input("enter 1st element"))
#b=int(input("enter 2nd element"))
#while b!=0:
#    a,b=b,a%b
#print("GCD of 2 number is:",a)
#write a code for find LCM
#a=int(input("enter the 1st element"))
#b=int(input("enter the 2nd element"))
#while b>0:
#    a,b=b,a%b
#print("LCM of 2 numbers is:",a)
#prime number or not
#n=int(input("enter the element"))
#a=0
#x=int(a**0.5)+1
#count=0
#if a==1:
#    print("number not is prime")
#elif a==2:
#    print("number is prime")
#else:
# for i in range(2,x):
#    if a%i==0 :
#        count=1
#        break
#if count==0:
#    print("a is prime")
#else:
#   print("a is not a prime")
#write a program to print all the prime numbers in a given range
a=int(input("enter the element"))
b=int(input("enter the element"))
for i in range(a,b+1):
   for j in range(2,i):
    if i%j==0:
        break
else:
    print(i)


