Code_Meli_Ha=[]
List_Bimarestan=[]
while True:
    Meno_Bimarestan=input("1)Nobat Dehi  2)Peygiri Nobat  3)Khoroj    ")
    if Meno_Bimarestan == "3":
        break

    match Meno_Bimarestan:
            case "1":
                Nam=input("Nam Va Nam Khanevadegi To Vared Kon:")
                while True:
                    code_Meli = input("Kode Melito Vared Kon (10 Raghami): ")
                    if code_Meli.isdigit() and len(code_Meli) == 10:
                        break
                    print("Eshtebah Zadi Ke!")
                Bakhsh=input("1)Dakheli  2)Govaresh 3)Poost Va Moo 4)Khoroj    ")
                match Bakhsh:
                    case "1":
                        Mablagh_Visit=100000
                        Khadamat=1.1
                        Jam=int(Mablagh_Visit*Khadamat)
                        print(f"Resid Shoma\nNam Va Nam Khanevadegi:\t{Nam}\nCode Meli:\t{code_Meli}\nBakhsh:\tDakheli\nMablagh:\t{Jam}Toman")
                        Code_Meli_Ha.append(code_Meli)
                        List_Bimarestan.append(f"{Nam}\t{code_Meli}\tDakheli\tpardakhti:{Jam}")
                        continue
                    case "2":
                        Mablagh_Visit=150000
                        Khadamat=1.1
                        Jam=int(Mablagh_Visit*Khadamat)
                        print(f"Resid Shoma\nNam Va Nam Khanevadegi:\t{Nam}\nCode Meli:\t{code_Meli}\nBakhsh:\tGovaresh\nMablagh:\t{Jam}Toman")
                        Code_Meli_Ha.append(code_Meli)
                        List_Bimarestan.append(f"{Nam}\t{code_Meli}\tGovaresh\tpardakhti:{Jam}")
                        continue
                    case "3":
                        Mablagh_Visit=250000
                        Khadamat=1.1
                        Jam=int(Mablagh_Visit*Khadamat)
                        print(f"Resid Shoma\nNam Va Nam Khanevadegi:\t{Nam}\nCode Meli:\t{code_Meli}\nBakhsh:\tPoost Va Moo\nMablagh:\t{Jam}Toman")
                        Code_Meli_Ha.append(code_Meli)
                        List_Bimarestan.append(f"{Nam}\t{code_Meli}\tGovaresh\tPoost Va Moo:{Jam}")
                        continue
                    case "4":
                        pass
            case "2":
                Peygiri_code=input("Code Meli Ke Nobat Gerefte Id Ra Vared Konid:")
                if Peygiri_code in Code_Meli_Ha:
                    Nobat=Code_Meli_Ha.index(Peygiri_code)+1
                    print (f"Shoma Nafar {Nobat} Hastin.")
                    print (List_Bimarestan[Nobat-1])
                else:
                    print("In Code Meli Nist!!!!")