def binarysearch(array,f,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if array[mid]==f:
            return mid
        elif array[mid]<f:
            low=mid+1
        else :
            high=mid-1
    return-1

array=[]
n=int(input())
for i in range(n):
    element=int(input("enter :"))
    array.append(element)
f = int(input("enter the value to find index :"))
result=binarysearch(array,f,0,len(array)-1)

if result!=-1:
    print("element is present at index" +str(result))
else:
    print("Not found")
