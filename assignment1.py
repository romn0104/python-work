Nameh_Amal=[]
Nomreh_ha = []
Esm=input("Esmet Chie?")
i=0
while i<10:
    Esm_Darset=input("Esme Darseto Begooooo:")
    Nomreh=float(input("Nomrat Chand Shod!?"))
    if 0>Nomreh or Nomreh>20:
        print("Mesle Adam Nomrato Bezan!")
        continue
    
    Nomreh_ha.append(Nomreh)
    if 15<=Nomreh<=20:
        if Nomreh == 20:
         Nameh_Amal.append(f"{Esm_Darset}\t{Nomreh}\tA+++\n")
        elif 20>Nomreh>=19:
           Nameh_Amal.append(f"{Esm_Darset}\t{Nomreh}\tA++\n")
        elif 19>Nomreh>=18:
            Nameh_Amal.append(f"{Esm_Darset}\t{Nomreh}\tA+\n")
        elif 18>Nomreh>=17:
            Nameh_Amal.append(f"{Esm_Darset}\t{Nomreh}\tA\n")  
        elif 17>Nomreh>=16:
            Nameh_Amal.append(f"{Esm_Darset}\t{Nomreh}\tB+\n")    
        elif 16>Nomreh>=15:
            Nameh_Amal.append(f"{Esm_Darset}\t{Nomreh}\tB\n") 
    elif 15>Nomreh>=10 :
        if 15>Nomreh>=14:
            Nameh_Amal.append(f"{Esm_Darset}\t{Nomreh}\tC+\n")
        elif 14>Nomreh>=13:
            Nameh_Amal.append(f"{Esm_Darset}\t{Nomreh}\tC\n")
        elif 13>Nomreh>=12:
            Nameh_Amal.append(f"{Esm_Darset}\t{Nomreh}\tD+\n")
        elif 12>Nomreh>=10:
            Nameh_Amal.append(f"{Esm_Darset}\t{Nomreh}\tD\n") 
    elif 0 <= Nomreh < 10:
        Nameh_Amal.append(f"{Esm_Darset}\t{Nomreh}\tMardood Shodi!\n")
    i += 1
Moadel=sum(Nomreh_ha)/len(Nomreh_ha)
Nameh_Amal.append(f"Moadelet:\t{Moadel}\t")
print(f"Nameh Amal {Esm} Aziz...")
print("".join(Nameh_Amal))                                                         