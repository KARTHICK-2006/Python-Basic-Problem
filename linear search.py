def linearseearch(li,key_value,n):
    for i in range(0,n):
        if(list1[i]==key_value):

            return i
    return-1
list1=[1,2,3,4,5]
f=4
n=(len(list1))
result=linearsearch(list1,f,n)
if(result==-1):
    print("element not found")
else:
    print("element found",result)
