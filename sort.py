numbers = []
 
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
 
    numbers.append(ele)
numbers.sort()
  
print(numbers)