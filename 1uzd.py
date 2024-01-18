#Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu.


with open('aa.txt', 'r') as fails: #izveidoju txt failu, kuru noradu iekavas, kā to kas jaatver. "r" ,jo jālasa
    teksts = fails.read()
    print(teksts)  #printe ara tekstu
