import random

#Liste, welche alle Optionen enthält
options = ["Schere", "Stein", "Papier"]

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

    #Auswahl des Computers
    computer_choice = options[random.randrange(0,2)]

    print(f"Spieler -->{player_choice}      Computer --> {computer_choice}")
        
    #Überprüfen wer gewonnen hat
    if player_choice == computer_choice:
        print("Ausgleich")

    elif player_choice == "Schere" and computer_choice == "Papier":
        print("Spieler hat gewonnen")
        
    elif player_choice == "Stein" and computer_choice == "Schere":
        print("Spieler hat gewonnen")
        
    elif player_choice == "Papier" and computer_choice == "Stein":
        print("Spieler hat gewonnen")
        
    else:
        print("Computer hat gewonnen")


        
        
