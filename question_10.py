#paasword verified mr.x trying to create a new password for his instagram account these are requried conditions for creating new password
#1)minimum length is 8,maximum length is 15
#2)only @ / is allowed in a password
#3)no spaces are allowed
#4)only alpha numeric are allowe
#5)suppose to print weak- if length is exact 8
#6)medium-length is between 8-12
#7)strong if length is between 12-15  
str=int(input())
count=0
strong=0
weak=0
a=len(str)
if a<=8:
    print(weak)
else:
    print(strong)
for i in str:
    if i = @ or /:
      count+=1
p=input()
x=len(p)
if(('@'and'/')in p and x==8 and " "not in p):
    print("weak")
elif(('@'and'/') in p and x>8 and x<12 and " "not in p):
    print("medium")
elif(('@'and'/') in p and x>12 and x<15 and " "not in p):
    print("strong")
else:
    print("follow the instructions")

   
