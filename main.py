"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michaela Tóthová
email: misatothova7@seznam.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',

    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

jmeno = input("username: ")
heslo = input("password: ")

if jmeno in registrovani_uzivatele and registrovani_uzivatele[jmeno] == heslo:
    print("----------------------------------------")
    print(f"Welcome to the app, {jmeno}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("----------------------------------------")

    vstup = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
    print("----------------------------------------")

    if not vstup.isdigit():
        print("Chyba: Zadaný vstup není číslo. Program končí.")
    else:
        index = int(vstup) - 1  
        if index < 0 or index >= len(TEXTS):
            print("Chyba: Zadané číslo textu není platné. Program končí.")
        else:
            vybrany_text = TEXTS[index]
            words = vybrany_text.split()
            cisla = [slovo for slovo in words if slovo.isdigit()]

            pocet_slov = len(words)
            pocet_titlecase = sum(1 for slovo in words if slovo.istitle())
            pocet_upper = sum(1 for slovo in words if slovo.isupper() and slovo.isalpha())
            pocet_lower = sum(1 for slovo in words if slovo.islower())
            pocet_cisel = len(cisla)
            soucet_cisel = sum(int(cislo) for cislo in cisla)

            print(f"There are {pocet_slov} words in the selected text.")
            print(f"There are {pocet_titlecase} titlecase words.")
            print(f"There are {pocet_upper} uppercase words.")
            print(f"There are {pocet_lower} lowercase words.")
            print(f"There are {pocet_cisel} numeric strings.")
            print(f"The sum of all the numbers {soucet_cisel}")
            print("----------------------------------------")
            print("LEN|  OCCURENCES  |NR.")
            print("----------------------------------------")

    
            delky = {}
            for slovo in words:
                l = len(slovo)
                delky[l] = delky.get(l, 0) + 1

            max_delka = max(delky.keys())
            for l in range(1, max_delka + 1):
                pocet = delky.get(l, 0)
                hvězdy = '*' * pocet
                print(f"{l:3}|{hvězdy:<18}|{pocet}")
else:
    print("\nunregistered user, terminating the program..")
