
file_path = 'aa.txt'  
with open(file_path, 'r', encoding="utf-8") as file:
    lines = file.readlines()
    if len(lines) >= 3:  #ja faaila ir pietiekami rindu
        print(f"Trešā rinda: {lines[2]}")
    else:
        print("Failā nav pietiekami daudz rindu.")
