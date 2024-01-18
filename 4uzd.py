nosaukums = input("Ievadi faila nosaukumu: ")
formats = input("Norādi faila formatu: ")

try:
    with open(nosaukums + '.' + formats, 'r') as fails:
        saturs = fails.read()
        print(saturs)
except FileNotFoundError:
    print("Fails netika atrasts!")
except IOError:
    print(" Nevarēja nolasīt failu!")
