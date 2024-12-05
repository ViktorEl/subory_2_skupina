

def nacitaj_subor(nazov_suboru):
    with open(nazov_suboru, 'r', encoding='utf-8') as f:
        nacitany = f.read()
        return nacitany
    
text = nacitaj_subor('ucitel.txt')
print(text)