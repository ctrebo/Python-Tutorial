import random

"""ToDo: Erstelle eine Liste, welche alle Optionen(Schere, Stein, Papier) als Strings enthält enthält"""
options = 

while True:

    #Überprüfen, ob der Spieler (noch) eine Runde spielen will
    play = input("Willst du eine Runde SCHERE STEIN PAPIER spielen? [j/n]: ").lower()
    while play != "j" and play != "n":
        play = input("Willst du eine Runde SCHERE STEIN PAPIER spielen? [j/n]: ").lower()

    if play == "n":
        break

    #Auswahl des Spielers
    player_choice = input("Wähle zwischen Schere, Stein, Papier :").capitalize()
    
    #Überprüfen, ob die Auswahl des Spielers gültig ist
    while player_choice not in options:
        player_choice = input("Wähle zwischen Schere, Stein, Papier :").capitalize()




    """ToDo: Aus der Liste options soll mithilfe des Index, welcher zufällig im Bereich von 0-2 gewählt werden soll, die Auswahl des
    Computers gewählt werden"""
    computer_choice = 

    """ToDo: Gib mithilfe von f'strings die Auswahl des Spielers(player_choice) und die Auswahl des Computers(computer_choice) aus"""
    print(f"  ")

    """ToDo: Überprüfe wer gewonnen hat, indem du players_choice mit computers_choice vergleichst(wie if a == 1 and b == 2:)
    Tipp: Du sparst dir viel Zeit, wenn du nur auf Ausgleich und Sieg des Spielers überprüfst, da der Rest(Sieg des Computers)
    mit else: abgedeckt werden kann"""
  



        
        
