vards = input(" ievadi savu vārdu: ")

try:
    with open("lietotajs.txt", 'w', encoding="utf-8") as fails:
        fails.write(vards)
    print("Vārds tika ierakstīts failā!")
except IOError:
    print(" Nevarēja ierakstīt failā!")
