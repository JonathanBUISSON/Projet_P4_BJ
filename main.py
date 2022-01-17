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
        player_1 = players[i]
        player_2 = players[i+1]
        print(player_1)  
        print(player_2)
        result_of_match = ViewMatch.get_match_result(None, player_1, player_2)
        #Pensez à mettre la ligne 22 en commentaire
        #result_2_of_match = ViewMatch.define_match(None, player_1, player_2)
        match = Match(player_1=player_1, player_2=player_2, result=result_of_match)
        
        #match_en_cours = Match.faire_match(player_1=player_1, player_2=player_2, result=result_of_match)

      #Tout ce qui est juste en dessous de cette ligne fonctionne
      #if match.result == str(0): #match.result (puis faire_match dans model)
      #     print(f"Les deux joueurs sont à égalité"),
      # if match.result == str(1):
      #    print(f"Le premier joueur a gagné et le deuxième joueur a perdu"),
      # elif match.result == str(2):
      # print(f"Le premier joueur a perdu et le deuxième a gagné")
        

        if match.result == str(0):
            print(f"Les deux joueurs sont à égalité"),
            while match.result != str(1) or match.result != str(2):
                res = input("Entrez le résultat du match:")
                if res == str(1):
                    print(f"le premier joueur a gagné et le second a perdu")
                    print(f"{player_1.first_name} a gagné et {player_2.first_name} a perdu.")
                    winners.append(player_1) 
                    losers.append(player_2) 
                    print(winners)
                    print(losers)
                    break
                elif res == str(2):
                    print(f"Le premier joueur a perdu et le second a gagné")
                    print(f"{player_1.first_name} a perdu et {player_2.first_name} a gagné.")
                    winners.append(player_2) 
                    losers.append(player_1) 
                    print(winners)
                    print(losers)
                    break
        elif match.result == str(1):
            print(f"le premier joueur a gagné et le second a perdu"),
            print(f"{player_1.first_name} a gagné et {player_2.first_name} a perdu.")
            winners.append(player_1)
            losers.append(player_2)
            print(winners)
            print(losers)
        elif match.result == str(2):
            print(f"Le premier joueur a perdu et le second a gagné"),
            print(f"{player_1.first_name} a perdu et {player_2.first_name} a gagné.")
            winners.append(player_2)
            losers.append(player_1)    
            print(winners)
            print(losers)
            
        #Faire un shuffle sur les winners et les losers.
        print("Affichage du mélange aléatoire des joueurs gagnants puis perdants:")
        random.shuffle(winners)
        print(winners)
        random.shuffle(losers)
        print(losers)

        j = 0
        while j < 4:
            player_1 = winners[j]
            player_2 = losers[j]
            #print(player_1)
            #print(player_2)
            print(f"{winners[j]} joue contre {losers[j]}")
            print(f"Si {winners[j]} perd contre {losers[j]} alors {winners[j]} prend la place de {losers[j]}") 
            break
        winners_demi_finale = []
        winners_quarts_de_finale = []
        losers_quarts_de_finale = []
         
        #print(f"Si {winners[j]} perd contre {losers[j]} alors {winners[j]} prend la place de {losers[j]}") 
        #print(f"{winners[j]} joue contre {losers[j]}")
        result_of_match = ViewMatch.get_match_result(None, player_1, player_2)
        match = Match(player_1=player_1, player_2=player_2, result=result_of_match)


        if match.result == str(0):
            print(f"Quarts_de_finale: Les deux joueurs sont à égalité"),
            while match.result != str(1) or quart_match.result != str(2):
                res = input("Entrez le résultat du match:")
                if res == str(1):
                    print(f"Au quart de finale: le premier joueur a gagné et le second a perdu")
                    print(f"Quarts_de_finale:{player_1.first_name} a gagné et {player_2.first_name} a perdu.")
                    winners_quarts_de_finale.append(player_1) 
                    losers_quarts_de_finale.append(player_2) 
                    print(winners_quarts_de_finale)
                    print(losers_quarts_de_finale)
                    winners_demi_finale.append(winners_quarts_de_finale)
                    break
                elif res == str(2):
                    print(f"Au quart de finale: le premier joueur a perdu et le second a gagné")
                    print(f"Quarts_de_finale:{player_1.first_name} a perdu et {player_2.first_name} a gagné.")
                    winners_quarts_de_finale.append(player_2) 
                    losers_quarts_de_finale.append(player_1) 
                    print(winners_quarts_de_finale)
                    print(losers_quarts_de_finale)
                    winners_demi_finale.append(winners_quarts_de_finale)
                    break
        elif match.result == str(1):
            print(f"Au quart de finale: le premier joueur a gagné et le second a perdu"),
            print(f"Quarts_de_finale:{player_1.first_name} a gagné et {player_2.first_name} a perdu.")
            winners_quarts_de_finale.append(player_1)
            losers_quarts_de_finale.append(player_2)
            print(winners_quarts_de_finale)
            print(losers_quarts_de_finale)
            winners_demi_finale.append(winners_quarts_de_finale)
        elif match.result == str(2):
            print(f"Au quart de finale: Le premier joueur a perdu et le second a gagné"),
            print(f"Quarts_de_finale:{player_1.first_name} a perdu et {player_2.first_name} a gagné.")
            winners_quarts_de_finale.append(player_2)
            losers_quarts_de_finale.append(player_1)    
            print(winners_quarts_de_finale)
            print(losers_quarts_de_finale)
            winners_demi_finale.append(winners_quarts_de_finale)
            
        print(winners_demi_finale)
        #random.shuffle(winners_quarts_de_finale)
        #print(winners_quarts_de_finale)

        #for k in range(0,2,2) and n in range(1,3,2): #Début n=1, fin n=3 et progression par pas de 2
        #for k in range(0,2,1): 
         #   player_1 = winners_quarts_de_finale[k]
         #   player_2 = winners_quarts_de_finale[n]
         #   print(player_1)
         #   print(player_2)
            
      #  result_2_of_match = ViewMatch.define_match(None, player_1, player_2)

      #  if result_2_of_match == str(0):
      #     print(f"{equals[0]} joue contre {equals[1]}" or f"{equals[1]} joue contre {equals[2]}" 
      #        or f"{equals[2]} joue contre {equals[3]}" or f"{equals[0]} joue contre {equals[3]}")

      #    print(f"{equals[0]} a gagné contre {equals[1]}"
      #       or f"{equals[1]} a gagné contre {equals[2]}" 
      #       or f"{equals[2]} a gagné contre {equals[3]}"
      #       or f"{equals[0]} a gagné contre {equals[3]}") #Je ne suis pas sûr pour celui-là

      # elif result_2_of_match == str(1):
      #    print(f"{winners[0]} joue contre {losers[0]}" or f"{winners[1]} joue contre {losers[1]}"
      #       or f"{winners[2]} joue contre {losers[2]}" or f"{winners[3]} joue contre {losers[3]}")
      #    print(f"{winners[0]} a gagné contre {losers[0]}"
      #       or f"{winners[1]} a gagné contre {losers[1]}"
      #       or f"{winners[2]} a gagné contre {losers[2]}"
      #       or f"{winners[3]} a gagné contre {losers[3]}")

      # elif result_2_of_match == str(2):
      #  print(f"{winners[0]} joue contre {losers[0]}" or f"{winners[1]} joue contre {losers[1]}"
      #      or f"{winners[2]} joue contre {losers[2]}" or f"{winners[3]} joue contre {losers[3]}")
      #   print(f"{winners[0]} a perdu face à  {losers[0]}"
      #       or f"{winners[1]} a perdu face à {losers[1]}"
      #       or f"{winners[2]} a perdu face à {losers[2]}"
      #       or f"{winners[3]} a perdu face à {losers[3]}")

      

           #print(f"{winners[1]} joue contre {losers[1]}")
           #print(f"{winners[1]} a perdu face à {losers[1]}")
        
        
    #print()
    #match = ViewMatch.create_match(object(),tournament, player_1, player_2) #players est une variable qui contient la liste all_players définit dans define_players
    
    #match.players = players
       