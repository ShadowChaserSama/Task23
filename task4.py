adlar = {}
i = 1

with open("adlar.txt", "w", encoding="utf-8") as file:
    while True:
        ad = input("Ad daxil edin (bitirmek ucun stop yazin): ")
        
        if ad.lower() == "stop":
            break
        
        file.write(ad + "\n")
        adlar[i] = ad
        i += 1

print("Dictionary:", adlar)
