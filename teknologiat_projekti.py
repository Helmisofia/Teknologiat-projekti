# -*- coding: cp1252 -*-

vaihtoehdot = ("(1) Lue muistikirjaa\n(2) Lis�� merkint�\n(3) Tyhjenn� muistikirja\n(4) Lopeta\n")

jatkuu = True

while jatkuu:
    print(vaihtoehdot)
    valinta = int(input("Mit� haluat tehd�?: "))
    
    if valinta == 1:
        tiedosto = open("muistio.txt","r")
        sisalto = tiedosto.read()
        print(sisalto, end='')
        tiedosto.close()

    if valinta == 2:
        tiedosto = open("muistio.txt","a")
        
        uusiteksti = str(input("Kirjoita uusi merkint�: "))
        tiedosto.write(str(uusiteksti)+"\n")
        tiedosto.close()

    if valinta == 3:
        tiedosto = open("muistio.txt","w")
        tiedosto.truncate(0)
        tiedosto.close()
        print("Muistio tyhjennetty.")

    if valinta == 4:
        tiedosto = open("muistio.txt","r")
        tiedosto.close()
        print("Lopetetaan.")
        jatkuu = False

