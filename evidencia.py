#registrovať vklad (kto, koľko) napr.: Karol, 5
#registrovať výber (kto, koľko) napr.: Karol, 120
#zistiť zostatok vo fonde
#zistiť zostatok podľa mena žiaka
#zistiť zostatky všetkých žiakov
#uložiť resp. načítať všetky pohyby v triednom fonde do resp. zo súboru.


def nacitaj_subor(nazov):
    with open(nazov, 'r', encoding='utf-8') as f:
        nacitany_subor = f.readlines()
        return nacitany_subor
    

def registruj_vklad(zoznam, meno, suma):
    zoznam.append(f'{meno}, {suma}\n')

def registruj_vyber(zoznam, meno, suma):
    zoznam.append(f'{meno}, -{suma}\n')

def zisti_zostatok(zoznam):
    zostatok = 0
    for prvok in zoznam:                       # 'Karol, 5\n'
        rozdeleny_retazec = prvok.split(',') # ['Karol', '5\n']
        suma = rozdeleny_retazec[1]            # '5\n'
        suma = float(suma)                     # 5
        zostatok = zostatok + suma
    return zostatok


def zisti_zostatok_podla_mena(zoznam, meno):
    zostatok = 0
    for prvok in zoznam:
        rozdeleny_prvok = prvok.split(',')  # ['Karol', '5\n']
        meno_ziaka = rozdeleny_prvok[0]     # 'Karol'
        suma = rozdeleny_prvok[1]           # '5\n'
        suma = float(suma)                  # 5
        if meno_ziaka == meno:
            zostatok += suma
    return zostatok
        

def zisti_zostatky(zoznam):
    slovnik = {}
    for prvok in zoznam:
        rozdeleny_prvok = prvok.split(',')
        meno = rozdeleny_prvok[0]
        suma = float(rozdeleny_prvok[1])
        if meno in slovnik:
            slovnik[meno] += suma
        else:
            slovnik[meno] = suma
    return slovnik


nacitany_subor = nacitaj_subor('fond.txt')
registruj_vklad(nacitany_subor, 'Jozo', 10)
registruj_vyber(nacitany_subor, 'Jozo', 5)
print(zisti_zostatok(nacitany_subor))
print(zisti_zostatok_podla_mena(nacitany_subor, 'Jozo'))
print(zisti_zostatky(nacitany_subor))
#print(nacitany_subor)


