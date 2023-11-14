import json
liste_køleskab = {}


def køleskab():
    try:
        with open("liste_køleskab.txt", "r", encoding="utf-8")as file:
            existing_data = json.load(file)
        
            liste_køleskab.update(existing_data)
    except FileNotFoundError:
        pass

    while True:
        a = input('brug disse for at navigere \n"t" = tilføj, \n"s" = slette'
                '\n"f" = find noget på listen \n"p" = print listen. \n"Q" = afslutte:\n')
        a = a.lower() #konventere teksten fra input til altid at være småt, således at if altid vil accaptere det
        
        if a == "p":
            print(liste_køleskab)
            
        elif a == "t":
            t = input("Tilføj genstand og antal:\n")
            t = t.lower() #gør første bogstav stort således brugeren ikke selv skal tænke på dette
            indhold = t.split()
            if len(indhold) == 2: #fortæller den længden af indholdet  
                key = indhold[0] #fortæller den at key er det første ord
                value = indhold[1]
                indhold = liste_køleskab[key] = value #indsætter det i Dict
            else:
                print("det var forkert, prøve igen\n")


        elif a == "s":
            if not liste_køleskab:
                print("det er ikke på listen, prøv ingen.")
            
            else:
                print(liste_køleskab)
                slet = input("hvad vil du slette?:\n")
                slet = slet.lower() #gør første bogstav stort således brugeren ikke selv skal tænke på dette
                if slet in liste_køleskab: #ser om det er i listen som skal slettes
                    del liste_køleskab[slet] #sletter fra listen
                else:
                    print(f'{slet} er ikke en del af listen prøv igen\n')

        elif a == "f":
            find_madvare = input("hvad søger du?:\n")
            find_madvare = find_madvare.lower() #gør første bogstav stort således brugeren ikke selv skal tænke på dette
            if find_madvare in liste_køleskab:
                print(f'{find_madvare} antal: {liste_køleskab[find_madvare]}')
            
            else:
                print(f'{find_madvare} findes ikke i listen')

        elif a == "q":
            print("farvel")
            break    

    with open("liste_køleskab.txt", "w", encoding="utf-8") as file:
         json.dump(liste_køleskab, file, ensure_ascii=False)

if __name__ == "__main__":
    køleskab()
    

