my_list=[1,-2,-13,4,16,-21]
my_list.append(9999)
my_list.insert(8,999)
print(len(my_list))
my_list.pop(2)
my_list_2=[5,6,7]
new_lst=my_list.copy()
print(my_list+my_list_2)
cnt=my_list.count(2)
print(cnt)
my_list.sort()
print(*my_list)
my_list=list(map(int,input().split("@")))
print(*my_list)
my_list=list(map(int,input().split("#")))
choice=int(input())
if(choice==1):
    print(my_list.append)
elif(choice==2):
    print(my_list.pop())
elif(choice==3):
    print(my_list.sort())
elif(choice==4):
    print(len(my_list))
else:
    print("good morning")


