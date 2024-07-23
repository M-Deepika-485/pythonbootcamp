#remove all the brackets from the given algebric expression
#str=input()
#for i in str:
#    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
#        pass
#    else:
#       print(i,end="")
#print()
#write a program to print next letters of given
#inp="ABC"
#char=''
#n=0
#for i in inp:
#    n=ord(i)
#    char+=chr(n+4)
#print(char)
#input=hello-----world then output should be -----helloworld
inp="hello-----wor---ld"
inp1=''
for i in inp:
    if(ord(i)==45):
        pass
    else:
        inp1+=i
print('-'*10+inp1)
