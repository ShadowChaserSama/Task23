total = 0
count = 0

with open("students.txt", "r") as file:
    for line in file:
        name, score = line.split()
        score = int(score)
        total += score
        count += 1

average = total / count

with open("average.txt", "w") as file:
    file.write(f"Qrupun ortalama bali: {average}")
