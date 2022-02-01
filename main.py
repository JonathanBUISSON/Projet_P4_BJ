from views import ViewPlayers, ViewTournament, ViewMatch
import random
from models import Match 

if __name__=='__main__':
    players = ViewPlayers.define_players() #appel aux méthodes de classe
    print(players)
    print()
    tournament = ViewTournament.define_tournament()
    tournament.players = players
    random.shuffle(players)
    winners = []
    losers = []
    for i in range(0,7,2):   #un pas de 2 (ainsi les jeux vont de 0, 2, 4 ,6 )
        print()
        player_1 = players[i]
        player_2 = players[i+1]
        print(player_1)  
        print(player_2)
        print()
        result_of_match = ViewMatch.get_match_result(None, player_1, player_2)
        match = Match(player_1=player_1, player_2=player_2, result=result_of_match)
        
        if match.result == str(0):
            print(f"Les deux joueurs sont à égalité"),
            while match.result != str(1) or match.result != str(2):
                res = input("Entrez le résultat du match:")
                if res == str(1):
                    print(f"le premier joueur a gagné et le second a perdu")
                    print()
                    print(f"{player_1.first_name} a gagné et {player_2.first_name} a perdu.")
                    winners.append(player_1) 
                    losers.append(player_2) 
                    print("Le(s) gagnant(s):", winners)
                    print("Le(s) perdant(s):", losers)
                    break
                elif res == str(2):
                    print(f"Le premier joueur a perdu et le second a gagné")
                    print()
                    print(f"{player_1.first_name} a perdu et {player_2.first_name} a gagné.")
                    winners.append(player_2) 
                    losers.append(player_1) 
                    print("Le(s) gagnant(s):", winners)
                    print("Le(s) perdant(s):", losers)
                    break
        elif match.result == str(1):
            print(f"le premier joueur a gagné et le second a perdu"),
            print()
            print(f"{player_1.first_name} a gagné et {player_2.first_name} a perdu.")
            winners.append(player_1)
            losers.append(player_2)
            print()
            print("Le(s) gagnant(s):", winners)
            print("Le(s) perdant(s):", losers)
        elif match.result == str(2):
            print(f"Le premier joueur a perdu et le second a gagné"),
            print()
            print(f"{player_1.first_name} a perdu et {player_2.first_name} a gagné.")
            winners.append(player_2)
            losers.append(player_1) 
            print()   
            print("Le(s) gagnant(s):", winners)
            print("Le(s) perdant(s):", losers)
    print()
    print("Affichage du mélange aléatoire des joueurs gagnants puis perdants:")
    random.shuffle(winners)
    print("Les gagnants sont:", winners)
    random.shuffle(losers)
    print("Les perdants sont:", losers)
    
    j = 0
    while j < 4 :
        player_1 = winners[j]
        player_2 = losers[j]
        print()
        print(f"{winners[j]} joue contre {losers[j]}") 
        j=j+1
        winners_quarts_de_finale = []
        losers_quarts_de_finale = []
        winners_demi_finale = []    
        result_of_match = ViewMatch.get_match_result(None, player_1, player_2)
        match = Match(player_1 = player_1, player_2=player_2, result=result_of_match)
           
        if match.result == str(0):
            print(f"Quarts_de_finale: Les deux joueurs sont à égalité"),
            while match.result != str(1) or match.result != str(2):
                res = input("Entrez le résultat du match:")
                if res == str(1):
                    print(f"Au quart de finale: le premier joueur a gagné et le second a perdu")
                    print()
                    print(f"Quarts_de_finale:{player_1.first_name} a gagné et {player_2.first_name} a perdu.")
                    winners_quarts_de_finale.append(player_1) 
                    losers_quarts_de_finale.append(player_2) 
                    print()
                    print("Le(s) gagnant(s):", winners_quarts_de_finale)
                    print("Le(s) perdant(s):", losers_quarts_de_finale)
                    for element in winners_quarts_de_finale:
                        #winners_demi_finale.append(element)
                        winners_demi_finale.extend(winners_quarts_de_finale)
                    print()
                    print("Le demi-finaliste est:", winners_quarts_de_finale)
                    break
                elif res == str(2):
                    print(f"Au quart de finale: le premier joueur a perdu et le second a gagné")
                    print()
                    print(f"Quarts_de_finale:{player_1.first_name} a perdu et {player_2.first_name} a gagné.")
                    winners_quarts_de_finale.append(player_2) 
                    losers_quarts_de_finale.append(player_1) 
                    print()
                    print("Le(s) gagnant(s):", winners_quarts_de_finale)
                    print("Le(s) perdant(s):", losers_quarts_de_finale)
                    for element in winners_quarts_de_finale:
                        #winners_demi_finale.append(element) 
                        winners_demi_finale.extend(winners_quarts_de_finale)
                    print()
                    print("Le demi-finaliste est:", winners_quarts_de_finale)
                    break
        elif match.result == str(1):
            print(f"Au quart de finale: le premier joueur a gagné et le second a perdu"),
            print()
            print(f"Quarts_de_finale:{player_1.first_name} a gagné et {player_2.first_name} a perdu.")
            winners_quarts_de_finale.append(player_1)
            losers_quarts_de_finale.append(player_2)
            print()
            print("Le(s) gagnant(s):", winners_quarts_de_finale)
            print("Le(s) perdant(s):", losers_quarts_de_finale)
            for element in winners_quarts_de_finale:
                #winners_demi_finale.append(element) 
                winners_demi_finale.extend(winners_quarts_de_finale)
            print()
            print("Le demi-finaliste est:", winners_quarts_de_finale)
        elif match.result == str(2):
            print(f"Au quart de finale: Le premier joueur a perdu et le second a gagné"),
            print()
            print(f"Quarts_de_finale:{player_1.first_name} a perdu et {player_2.first_name} a gagné.")
            winners_quarts_de_finale.append(player_2)
            losers_quarts_de_finale.append(player_1)
            print()    
            print("Le(s) gagnant(s):", winners_quarts_de_finale)
            print("Le(s) perdant(s):", losers_quarts_de_finale)
            for element in winners_quarts_de_finale:
                #winners_demi_finale.append(element)
                winners_demi_finale.extend(winners_quarts_de_finale)
            print()
            print("Le demi-finaliste est:", winners_quarts_de_finale)
    print()
    print("Affichage des gagnants de quarts de finale:")
    random.shuffle(winners_quarts_de_finale)
    print(winners_quarts_de_finale)
    print(winners_demi_finale)
    
    Noms_des_demi_finalistes=[]
    demi_finalistes = []
   
    demi_finalistes = input("Entrez le premier demi-finaliste:")
    Noms_des_demi_finalistes.append(demi_finalistes)
    demi_finalistes = input("Entrez le deuxième demi-finaliste:")
    Noms_des_demi_finalistes.append(demi_finalistes)
    demi_finalistes = input("Entrez le troisième demi-finaliste:")
    Noms_des_demi_finalistes.append(demi_finalistes)
    demi_finalistes = input("Entrez le quatrième demi-finaliste:")
    Noms_des_demi_finalistes.append(demi_finalistes)
    
    print(Noms_des_demi_finalistes[0])
    print(Noms_des_demi_finalistes[1])
    print(Noms_des_demi_finalistes[2])
    print(Noms_des_demi_finalistes[3])
    
    player_1 = Noms_des_demi_finalistes[0]
    player_2 = Noms_des_demi_finalistes[1]
    print(f"{Noms_des_demi_finalistes[0]} joue contre {Noms_des_demi_finalistes[1]}")
    result_of_match = ViewMatch.get_match_demi_finale_result(None, player_1, player_2)
    match = Match(player_1=player_1, player_2=player_2, result=result_of_match)

    #C'est à partir d'ici qu'il faut revoir: pourquoi winners_demi_finale.append(winners_quarts_de_finale) ne fonctionne pas ?
    
    #for elem in petit_boucle: \for element in winners_quarts_de_finale
    #grand_boucle.append(elem)  \winners_demi_finale.append(player)
    
    winners_premiere_demi_finale = []
    losers_premiere_demi_finale = []
    
    if match.result == str(0):
        print(f"Les deux joueurs sont à égalité"),
        while match.result != str(1) or match.result != str(2):
            res = input("Entrez le résultat du match:")
            if res == str(1):
                print(f"le premier joueur a gagné et le second a perdu")
                print()
                print(f"{player_1} a gagné et {player_2} a perdu.")
                winners_premiere_demi_finale.append(player_1) 
                losers_premiere_demi_finale.append(player_2) 
                print("Le gagnant:", winners_premiere_demi_finale)
                print("Le perdant:", losers_premiere_demi_finale)
                break
            elif res == str(2):
                print(f"Le premier joueur a perdu et le second a gagné")
                print()
                print(f"{player_1} a perdu et {player_2} a gagné.")
                winners_premiere_demi_finale.append(player_2) 
                losers_premiere_demi_finale.append(player_1) 
                print("Le gagnant:", winners_premiere_demi_finale)
                print("Le perdant:", losers_premiere_demi_finale)
                break
    elif match.result == str(1):
        print(f"le premier joueur a gagné et le second a perdu"),
        print()
        print(f"{player_1} a gagné et {player_2} a perdu.")
        winners_premiere_demi_finale.append(player_1)
        losers_premiere_demi_finale.append(player_2)
        print()
        print("Le gagnant:", winners_premiere_demi_finale)
        print("Le perdant:", losers_premiere_demi_finale)
    elif match.result == str(2):
        print(f"Le premier joueur a perdu et le second a gagné"),
        print()
        print(f"{player_1} a perdu et {player_2} a gagné.")
        winners_premiere_demi_finale.append(player_2)
        losers_premiere_demi_finale.append(player_1) 
        print()   
        print("Le gagnant:", winners_premiere_demi_finale)
        print("Le perdant:", losers_premiere_demi_finale) 
    print()
    print("Le premier demi-finaliste est:", winners_premiere_demi_finale)   
    print()

    player_1 = Noms_des_demi_finalistes[2]
    player_2 = Noms_des_demi_finalistes[3]
    print(f"{Noms_des_demi_finalistes[2]} joue contre {Noms_des_demi_finalistes[3]}")
    result_of_match = ViewMatch.get_match_demi_finale_result(None, player_1, player_2)
    match = Match(player_1=player_1, player_2=player_2, result=result_of_match)

    winners_deuxieme_demi_finale = []
    losers_deuxieme_demi_finale = []
    
    if match.result == str(0):
        print(f"Les deux joueurs sont à égalité"),
        while match.result != str(1) or match.result != str(2):
            res = input("Entrez le résultat du match:")
            if res == str(1):
                print(f"le premier joueur a gagné et le second a perdu")
                print()
                print(f"{player_1} a gagné et {player_2} a perdu.")
                winners_deuxieme_demi_finale.append(player_1) 
                losers_deuxieme_demi_finale.append(player_2) 
                print("Le gagnant:", winners_deuxieme_demi_finale)
                print("Le perdant:", losers_deuxieme_demi_finale)
                break
            elif res == str(2):
                print(f"Le premier joueur a perdu et le second a gagné")
                print()
                print(f"{player_1} a perdu et {player_2} a gagné.")
                winners_deuxieme_demi_finale.append(player_2) 
                losers_deuxieme_demi_finale.append(player_1) 
                print("Le gagnant:", winners_deuxieme_demi_finale)
                print("Le perdant:", losers_deuxieme_demi_finale)
                break
    elif match.result == str(1):
        print(f"le premier joueur a gagné et le second a perdu"),
        print()
        print(f"{player_1} a gagné et {player_2} a perdu.")
        winners_deuxieme_demi_finale.append(player_1)
        losers_deuxieme_demi_finale.append(player_2)
        print()
        print("Le gagnant:", winners_deuxieme_demi_finale)
        print("Le perdant:", losers_deuxieme_demi_finale)
    elif match.result == str(2):
        print(f"Le premier joueur a perdu et le second a gagné"),
        print()
        print(f"{player_1} a perdu et {player_2} a gagné.")
        winners_deuxieme_demi_finale.append(player_2)
        losers_deuxieme_demi_finale.append(player_1) 
        print()   
        print("Le gagnant:", winners_deuxieme_demi_finale)
        print("Le perdant:", losers_deuxieme_demi_finale) 
    print()
    print("Le deuxieme demi-finaliste est:", winners_deuxieme_demi_finale) 
    print()

    ### Ceci est la partie qui détermine le finaliste ###

    player_1 = winners_premiere_demi_finale
    player_2 = winners_deuxieme_demi_finale
    print(f"{winners_premiere_demi_finale} joue contre {winners_deuxieme_demi_finale}")
    result_of_finale = ViewMatch.get_match_finale_result(None, player_1, player_2)
    match = Match(player_1=player_1, player_2=player_2, result=result_of_finale)

    winner_finale =[]
    loser_finale = []

    if match.result == str(0):
        print(f"Les deux joueurs sont à égalité"),
        while match.result != str(1) or match.result != str(2):
            res = input("Entrez le résultat du match:")
            if res == str(1):
                print(f"le premier joueur a gagné et le second a perdu")
                print()
                print(f"{player_1} a gagné et {player_2} a perdu.")
                winner_finale.append(player_1) 
                loser_finale.append(player_2) 
                print("Le gagnant:", winner_finale)
                print("Le perdant:", loser_finale)
                break
            elif res == str(2):
                print(f"Le premier joueur a perdu et le second a gagné")
                print()
                print(f"{player_1} a perdu et {player_2} a gagné.")
                winner_finale.append(player_2) 
                loser_finale.append(player_1) 
                print("Le gagnant:", winner_finale)
                print("Le perdant:", loser_finale)
                break
    elif match.result == str(1):
        print(f"le premier joueur a gagné et le second a perdu"),
        print()
        print(f"{player_1} a gagné et {player_2} a perdu.")
        winner_finale.append(player_1)
        loser_finale.append(player_2)
        print()
        print("Le gagnant:", winner_finale)
        print("Le perdant:", loser_finale)
    elif match.result == str(2):
        print(f"Le premier joueur a perdu et le second a gagné"),
        print()
        print(f"{player_1} a perdu et {player_2} a gagné.")
        winner_finale.append(player_2)
        loser_finale.append(player_1) 
        print()   
        print("Le gagnant:", winner_finale)
        print("Le perdant:", loser_finale) 
    print()
    print("Le Finaliste du Tournoi d'Echec Suisse est:", winner_finale) 
    print("Félicitations", winner_finale,"tu as remporté le tournoi !")
       
    #print()
    #match = ViewMatch.create_match(object(),tournament, player_1, player_2) #players est une variable qui contient la liste all_players définit dans define_players
    
    #match.players = players
       