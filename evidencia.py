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
    for prvok in zoznam:
        pass


nacitany_subor = nacitaj_subor('fond.txt')
registruj_vklad(nacitany_subor, 'Jozo', 10)
registruj_vyber(nacitany_subor, 'Jozo', 5)
print(nacitany_subor)


