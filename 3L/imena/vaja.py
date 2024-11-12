#napiši program, ki prebere vsa števila iz te datoteke. Izračunaj povprečje vseh števil. Zapiši števila, ki so nad povprečjem v datoteko nad_povprecjem.txt, in števila, ki so pod povprečjem, v pod_povprecjem.txt

def razdeli_po_povprecju():
    with open("stevila.txt","r") as f:
        vrstice = f.readlines()
    
    stevila = [ ]
    for vrstica in vrstice:
        stevila.append(int(vrstica.strip()))
        
    povprecje = 0
    for i in stevila:
        povprecje += i
    
    povprecje = povprecje / len(stevila)
    
    with open("pod_povprecjem.txt","w") as pod_povprecjem_file, open("nad_povprecjem.txt" ,"w") as nad_povprecjem_file:
        for stevilo in stevila:
            if (stevilo < povprecje):
                pod_povprecjem_file.write(stevilo+"\n")
            else:
                nad_povprecjem_file.write(stevilo+"\n") 
    
razdeli_po_povprecju()

