#6

result1 = 2
result1 = result1*result1
result1 = result1+result1
result1 = result1*result1
print(result1)

#7
result2 = 100
for i in range(4, 8):
    result2 = result2 - i
print(result2)

#8
result3 = 100
for i in range(3, 8):
    if (i%2) == 0: 
        result3 = result3 - i
print(result3)

#9
def minVal5(array):
    array.sort()
    return array[4]

nums = [15, 14, 13, 12, 11, 20, 19, 18, 17, 16]
print(minVal5(nums))

#10
#Option1 - without recursion
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result
#test
print(factorial(10))

#Option2 - with recursion
def factorialRecursion(n):
    result = 1
    if n > 1:
        result = n * factorialRecursion(n-1)
    return result
#test
print(factorialRecursion(10))