

def nacitaj_subor(nazov_suboru):
    with open(nazov_suboru, 'r', encoding='utf-8') as f:
        nacitany = f.read()
        return nacitany
    

def vytvor_diktat(text, zoznam_symbolov):
    diktat_ziak = ''
    for pismeno in text:
        if pismeno in zoznam_symbolov:
            diktat_ziak = diktat_ziak + '_'
        else:
            diktat_ziak = diktat_ziak + pismeno
    return diktat_ziak

def uloz_do_suboru(nazov_suboru, diktat):
    with open(nazov_suboru, 'w', encoding='utf-8') as f:
        f.write(diktat)

text = nacitaj_subor('ucitel.txt')
symboly = ['i', 'y', 'ý', 'y', 'I', 'Y']
diktat_ziak = vytvor_diktat(text, symboly)
uloz_do_suboru('ziak.txt', diktat_ziak)


