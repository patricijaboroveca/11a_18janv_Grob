import csv
file_path = 'bb.csv'  # aizstāj ar faila celu

try:
    with open(file_path, 'r', encoding="utf-8") as csv_fails:
        csv_lasitajs = csv.reader(csv_fails)
        
        for row in csv_lasitajs:
            #parbauda vai vispar ir pietiekami kollonu
            if len(row) >= 2:
                second_column_data = row[1]
                print(f"Otrās kolonnas dati: {second_column_data}")
            else:
                print("nav pietiekams saturs")
except FileNotFoundError:
    print(f"Fails {file_path} netika atrasts.")

