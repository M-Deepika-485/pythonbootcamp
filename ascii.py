ascii
print(ord('A'))
print(ord('A')+3)
print(ord('a'))
print(ord('0'))
print(char(0))
#check how many vowels are there in string
str=['a','e','i','o','u']
count=0
inp="deepika"
for i in inp:
      if(i in stvowelr):
        count+=1
print(count)

#write a program for consonent count
str=['a','e','i','o','u']
count=0
inp="deepika"
for i in inp:
      if(i not in str):
        count+=1
print(count)

#write a program to print vowel and consonent
#vowel="aeiou"
#consonent="dbgrtyjkh"
#count=0
#c=0
#inp="helloworld"
#for i in inp:
#    if i in vowel:
#        count+=1
#print(count)
#for i in inp:
#    if i not in vowel:
#        c+=1
#print(c)
#print all the vowels follwed by consonents 
#vowel="aeiou"
#consonent="bcdfghjklmnpqrstvwxyz"
#ans=""
#inp="deepika"
#for i in inp:
#    if i in vowel:
#        ans+=i
#print(ans)
#for i in inp:
#    if i in consonent:
#        ans+=i
#print(ans)

#print the unique characters in a string
#vowel="aeiou"
#consonent="bcdfghjklmnpqrstvwxyz"
#ans=""
#inp="deepika"
#for i in inp:
#    if i not in ans:
#        ans+=i
#print(ans)
#string sum
#inp="deepika"
#ans=""
#sum=0
#for i in inp:
#    if i not in ans:
#        ans+=i
#       sum+=1
#print("sum of ans",sum)
#reverse the string
#i="1234"
#rev=""
#for i in range:
#    r=i%10
#   rev=rev+str(r)
#    i=i//10
#ans=int(rev)
#print(ans)
#ascii numbers
#for i in range(32,128):
#    print(chr(i),end=" ")
#ascess the elements using ascii values
#inp=input()
#sum=0
#for i in inp:
#    if (ord(i)>=48 and ord(i)<=57):
#        sum+=int(i)
#print(sum)
#write a code to print all capital letters in the given string
#inp=input()
#for i in inp:
#    if (ord(i)>=65 and ord(i)<=97):
#        print(i)








