n = int(input('Enter the number of the start line of copying:'))
k = int(input('Enter the number of the end line of copying:'))
count = 0
data = ''

with open(r"D:\courses\Practic\hw4_f1.txt", encoding="utf8") as file1:
    line = file1.readline()
    for line in file1:
        count += 1
        if count > n - 1:
            data += line
        if count == k:
            break

file2 = open(r"D:\courses\Practic\hw4_f2.txt", "w", encoding="utf8")
file2.write(data)
file2.close()

print(data)

consonant = ['й', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'ь', 'б']
count_consonant = 0

for letter in data:
    if letter in consonant:
        count_consonant += 1
print(count_consonant)
