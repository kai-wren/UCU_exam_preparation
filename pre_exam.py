from array import array

result1 = 2
result1 = result1*result1
result1 = result1*result1
result1 = result1*result1
print(result1)

result2 = 100
for i in range(3, 8):
    result2 = result2 - i
print(result2)

result3 = 100
for i in range(3, 8):
    if (i%2) == 0: 
        result3 = result3 - i
print(result3)

x4 = 2
y4 = 3
z4 = 4
if x4 > y4:
    z4 = z4 + x4
else:
    z4 = z4 + y4
print(z4)

x5 = 2
for i in range(3, 7):
    x5 = x5*x5
print(x5)

x6 = 1
for i in range(3, 8):
    for j in range(2, i):
        if (i%j) == 0:
            break
    else:
        x6 = x6*i
print(x6)

def func1(list):
    list.sort(reverse=True)
    print(list[2])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func1(nums)

