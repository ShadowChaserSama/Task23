words = input("Sozleri bosluqla daxil edin: ")
words_list = words.split()
result = {}

for word in words_list:
    result[word] = word.upper()

print(result)
