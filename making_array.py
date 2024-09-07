num=int(input("Enter a number: "))
arr=[]
for i in range(num):
    element=(int(input(f"enter element {i+1}: ")))
    arr.append(element)#(int(input(f"enter element {i+1}: ")))
    arr.sort()
for i in range(num):
    print(f"the {i+1} element of array is {arr[i]}")
print(arr)