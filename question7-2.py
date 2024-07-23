#your are given with a space separted with integer list find no.of of even elements and no.f of odd elements in a given list
my_list=list(map(int,input().split()))
even=0
odd=0
for i in range(0,len(my_list)):
    if(my_list[i]%2==0):
        even+=1
    else:
        odd+=1
print(even,odd)
#