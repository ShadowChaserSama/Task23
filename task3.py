text = input("Metn daxil edin: ")

reqemler = "0123456789"
herfler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = {"herf": 0, "reqem": 0}

for ch in text:
    if ch in reqemler:
        result["reqem"] += 1
    elif ch in herfler:
        result["herf"] += 1

print("Herflerin sayi:", result["herf"])
print("Reqemlerin sayi:", result["reqem"])
