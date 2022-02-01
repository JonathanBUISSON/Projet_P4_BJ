
from models import Player, Tournament, Match 
import random
import time


class ViewPlayers:
    
    def define_players():
        all_players = []
        for i in range(1,9):
            first_name = input("Veuillez entrer le prénom du player:")
            last_name = input("Veuillez entrer le nom du player:")
            gender = input("Veuillez entrer le sexe du player: Homme ou Femme?")
            birthdate = input("Veuillez entrer une date de naissance sous la forme Day/Month/Year:")
            ranking = input("Veuillez entrer le classement du player:")
            current_player = Player(first_name, last_name, gender, birthdate, ranking, 0, i) #instance de l'objet player
            all_players.append(current_player)
        return all_players


class ViewTournament:

    def define_tournament():   
        tournament_name_input = input("Veuillez entrer le nom du tournoi: ")
        location_input = input("Veuillez entrer le lieu du tournoi: ")
        tournament_date_input = input("Veuillez entrer la date du tournoi: ")
        time_control_input = input("Veuillez entrer le contrôle du temps: ")
        description_input = input("Veuillez entrer la description du tournoi: ")
        tournament_id_input = input("Veuillez entrer l'Id du tournoi: ")
        current_tournament = Tournament(tournament_name = tournament_name_input, location = location_input, tournament_date = tournament_date_input, 
                                        time_control = time_control_input, description = description_input, 
                                        tournament_id = tournament_id_input) 
        
        return current_tournament 
    
    
 #Rajout cette semaine de display_tournament_time
    def display_tournament_time(self):
        print()
        input("Appuyer sur une touche pour commencer le tour") 
        print()
        begin_time = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))  # %d jour du mois sur deux chiffres, %m Numéro du mois sur deux chiffres %Y année complète sur 4 chiffres.
        print(f"Début du tour : {begin_time}")                      # %H heure à deux chiffres, %M minutes sur deux chiffres, %S Seconde sur deux chiffres.
        print()
        input("Appuer sur une touche lorsque le tour est terminé")
        print()
        end_time = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        print(f"Fin du tour: {end_time}")
        print()
        return begin_time, end_time

class ViewMatch:

   #def define_match(player_1, player_2): #player_1 et player_2 enregistrer le resultat dans l'objet match
            #Table_of_players=[]
            #match_name_input = input("Veuillez entrer le nom et le numero du match:") #Exemple: Nom = Round 1
        
            #if player_1 == player_2:
            #    print("Match impossible")
            #else: 
            #print(f"Le match a lieu entre {player_1.last_name} et {player_2.last_name}")
            #print(match entre les deux joueurs et le résultat du match)
               # Table_of_players.append(player_1.last_name)
                #Table_of_players.append(player_2.last_name)
                #print(Table_of_players)   
            #match_result = input("Veuillez rentrer le resultat du match:")
            #return d'un objet match qui aura player1 et player2 et résultat / apres on boucle pour avoir les 4 match, la boucle se trouve dans main pas dans view

 def get_match_result(self, player_1, player_2): 
    print(f"Le match a lieu entre {player_1.first_name} et {player_2.first_name}")
    result = input("Entrez le resultat du premier joueur:")
    return result #instance de la classe match

 def get_match_demi_finale_result(self, player_1, player_2):
    print(f"Le match de demi-finale a lieu entre {player_1} et {player_2}")
    result = input("Entrez le résultat du premier joueur:")
    return result

 def get_match_finale_result(self, player_1, player_2):
    print(f"Le match final a lieu entre {player_1} et {player_2}")
    result = input("Entrez le résultat du premier joueur:")
    return result

 def create_match(turn,tournament, player_1, player_2):
    players = tournament.players
    players_sorted = sorted(players, key=lambda x:x.ranking)
    length_players = len(players_sorted)

    half_length_players = int(length_players / 2)
    players_first_half = players_sorted[:half_length_players]
    players_second_half = players_sorted[half_length_players:length_players]

    i = 0
    j = 0
    turn.matchs = []
  
    while i <= length_players and j <= (length_players/2)-1 :
     
      player_1 = players_first_half[j]
      player_2 = players_second_half[j]

    tuple_match =([player_1,0] ,[player_2, 0])
    print("============================================")
    print(f"player_1: {tuple_match[0][0]}, score 1: {tuple_match[0][1]}, player_2: {tuple_match[1][0]}, score 2: {tuple_match[1][1]}")
    print("============================================")
    j= j + 1
    i = i + 1
    print("============================")
