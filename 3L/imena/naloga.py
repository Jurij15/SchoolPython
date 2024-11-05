def razdeli_imena():
    with open("imena.txt", "r") as f:
        vrstice = f.readlines()
        
    with open("imena_A_M.txt","w") as a_m_file, open("imena_n_z.txt" ,"w") as n_z_file:
        for vrstica in vrstice:
            ime = vrstica.strip()
            if(ime[0].upper() <= "M"):
                a_m_file.write(ime+"\n")
            else:
                n_z_file.write(ime+"\n")

razdeli_imena()