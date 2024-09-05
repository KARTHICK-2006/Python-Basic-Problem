k=int(input())
found=False
for i in range(len(li)):
    if li[i]==k:
        found=True
        break
if found==True:
    print("Element found in order",i)
else:
    print("not order",i)
