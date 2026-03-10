with open("adlar.txt", "w") as f:
    adlar = input("Adlari bosluqla daxil edin: ")
    f.write(adlar)

with open("adlar.txt", "r") as f:
    metn = f.read()
    sozler = metn.split()
    print("Sozlerin sayi:", len(sozler))
