import random
tajne_cislo=random.randint(1, 10)
tip=0
while tip != tajne_cislo:
    tip=int(input("Zadejte číslo: "))
    if tip > tajne_cislo:
        print("Zkus míň")
    elif tip < tajne_cislo:
        print("Zkus víc")
    else:
        print("Grutuluji, uhádl jsi tajné číslo")



