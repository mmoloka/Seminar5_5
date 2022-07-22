# В файле находятся N натуральных чисел, записанных через пробел. Средичисел не хватает одного чтобы выыполнить условие
# A [i] - 1 = A [i - 1]. Найдите это число

with open('1.txt', 'r') as file:
    arr = file.readlines()
    arr = [int(i) for i in arr[0].split()]
    for i in range(1, len(arr)):
        if arr[i] - 1 != arr[i - 1]:
            print((arr[i] + arr[i - 1]) // 2)
