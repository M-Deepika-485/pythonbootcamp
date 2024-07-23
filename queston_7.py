#your are given with a comma separeted natural numbers 1-10 print omy_list=list(map(int,input().split()))
my_list=list(map(int,input().split()))
count=0
for i in range(0,len(my_list),2):
#    print(i)
 count+=1
print(count)