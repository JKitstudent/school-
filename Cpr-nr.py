#kontrol af cpr nummerets længde
def er_cpr_gyldigt(cpr):
    if len(cpr) !=10:
        return False
    


    #liste med antal af dage i hver mående 
    ml = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #opdel cpr nummert i dag, mående, år.
    dag = int(cpr[0:2])
    måned = int(cpr[2:4])

    #tjek om måneden er gyldig (1-12)
    if måned < 1 or måned > 12:
        return False

    #hent månedeslængden for den pågældende månede
    månedeslængde = ml[måned - 1]

    #kontrollere om dagen er gyldig
    if dag < 1 or dag > månedeslængde:
        return False

    #hvis alle er bestået er det true
    return True

def køn_udfra_cpr(cpr):
    #ekstraher de sidste fire fra cpr-nr.
    sidste_fire = int(cpr[-1:])
    #kontrollere om det sidste tal er lige eller ulige
    if sidste_fire % 2 == 0:
        return 'Kvinde' #hvis de er lige så er det en kvinde
    else:
        return 'Mand' #hvis de er ulige er det en mand

#liste til at gemme alle gyldige cpr-nr til print til sidst
gyldige_cpr = []

while True:
    cpr = (input('indtast et cpr-nummer eller "q" for at afslutte:\n'))

    if cpr.lower() == 'q':
        break

    if er_cpr_gyldigt(cpr):
        køn = køn_udfra_cpr(cpr)
        print(f'{cpr} er gyldigt, tilhøre en {køn}')
        #gyldige cpr-nr bliver gemt i listen.
        gyldige_cpr.append((cpr, køn))

    else:
        print(f'{cpr} er ikke gyldigt!')

#gyldige cpr-nr som er gemt, udskrives til sidst, for at gøre det overskueligt.        
print('Gyldige CPR-numre:')
for cpr, køn in gyldige_cpr:
    print(f' CPR-nummer: {cpr}, køn: {køn}')    

