"""
                                                        Zahl erraten

Mithilfe der Random-Bibliothek soll ein kleines Spiel programmiert werden, bei dem der Spieler eine Zahl
in einem gewissen Bereich erraten soll                                                    
"""

import random

while True:
    #Eine Zufallszahl in einem gewissen Bereich soll in eine Variable gespeichert werden
    number = random.randrange(1,10)
    print(number)
    #Der Spieler wird aufgefordert, die Zahl zu erraten. Dafür wird ein input-Befehl verwendet und in eine Variable gespeichert.
    guess = int(input("Errate die Zahl! : "))
    #Verwende den if/else Befehl, um die Vermutung mit der tatsächlichen Zahl zu vergleichen!
    if number == guess:
        print("Richtig!")
    else:
        print("Falsch!")