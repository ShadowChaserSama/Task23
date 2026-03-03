numbers = input("Ededleri bosluqla daxil edin: ")
numbers_list = numbers.split()
result = {}

for num in numbers_list:
    n = int(num)
    result[n] = n ** 2

print(result)
