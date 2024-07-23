#my_list=list(map(int,input().split()))
#temp=my_list[0]
#for i in range(len(my_list)):
#    if(my_list[i]>temp):
#        temp=my_list[i]
#        print(temp)
 #find the minimum value of the given list       
#my_list=list(map(int,input().split()))
#temp=my_list[0]
#for i in range(len(my_list)):
#    if(my_list[i]<temp):
#        temp=my_list[i]
#print(temp)
#replace the elements in an array with average of maximum and minimum elements
#my_list=list(map(int,input().split()))
#temp=my_list[0]
#max=my_list[0]
#min=my_list[0]
#for i in range(len(my_list)):
#    if(my_list[i]>temp):
#        max=my_list[i]
#    if(my_list[i]<temp):
#        min=my_list[i]
#avg=(max+min)/2
#for i in range(len(my_list)):
#    my_list[i]=avg
#print(*my_list)    
#find the missing number in an array
#my_list=[1,2,3,4,5,7,8,9,10]
#n=len(my_list)
#total_sum=(n+1)*(n+2)/2
#sum=0
#for i in range(len(my_list)):
#    sum+=my_list[i]
#print(total_sum-sum)
#find the dupicates in an array
my_list=list(map(int,input().split()))
for i in my_list:
    if(i not in my_list[i]):
        my_list[i].append(i)
print(my_list[i])  



  

