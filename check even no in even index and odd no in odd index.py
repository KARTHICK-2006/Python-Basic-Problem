list1=[2,1,4,3,6,7,6,3]
list2=[]
print("original list of number:",list1)
for i in range(len(list1)):
    if(list1[i]%2==i%2):
        list2.append(list1[i])
if(list1==list2):
    print("True")
else:
    print("false")
