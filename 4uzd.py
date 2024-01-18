nosaukums = input("Ievadi faila nosaukumu: ")
formats = input("Norādi faila formatu: ")

try:
    with open(nosaukums + '.' + formats, 'r') as fails:  #atverot lasa nosaukumu un saturu
        saturs = fails.read()
        print(saturs)
except FileNotFoundError:               #kludas
    print("Fails netika atrasts!")
except IOError:
    print(" Nevarēja nolasīt failu!")
