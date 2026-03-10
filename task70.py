total = 0
count = 0

with open("students.txt", "r") as file, open("kesilenler.txt", "w") as fail_file:
    for line in file:
        name, score = line.split()
        score = int(score)

        total += score
        count += 1

        if score < 50:
            fail_file.write(name + "\n")

average = total / count

with open("average.txt", "w") as file:
    file.write(f"Qrupun ortalama bali: {average}")
