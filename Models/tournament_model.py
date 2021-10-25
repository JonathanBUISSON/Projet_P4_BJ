from tinydb import TinyDB


tournament_database = TinyDB('models/tournament.json')


class Tournament:
    """Use to create an instance of a tournament"""
    def __init__(self, tournament_name=None,
                 location=None,
                 tournament_date=None,
                 number_of_tours=4,
                 time_control=None,
                 description=None,
                 players_ids=None,
                 list_of_tours=[],
                 tournament_id=None
                 ):

        self.tournament_name = tournament_name
        self.location = location
        self.tournament_date = tournament_date
        self.number_of_tours = number_of_tours
        self.time_control = time_control
        self.description = description
        self.players_ids = players_ids
        self.list_of_tours = list_of_tours
        self.tournament_id = tournament_id

    def __repr__(self):
        return f"{self.tournament_name} - {self.location}\n\n {self.list_of_tours}\n"

    def serialized(self):
        tournament_infos = {}
        tournament_infos['Nom du tournoi'] = self.tournament_name
        tournament_infos['Lieu'] = self.location
        tournament_infos['Date'] = self.tournament_date
        tournament_infos['Nombre de tours'] = self.number_of_tours
        tournament_infos['Controle du temps'] = self.time_control
        tournament_infos['Description'] = self.description
        tournament_infos["Joueurs_id"] = self.players_ids
        tournament_infos["Tours"] = self.list_of_tours
        tournament_infos["Id du tournoi"] = self.tournament_id

        return tournament_infos

    def unserialized(self, serialized_tournament):
        tournament_name = serialized_tournament['Nom du tournoi']
        location = serialized_tournament['Lieu']
        tournament_date = serialized_tournament['Date']
        number_of_tours = serialized_tournament['Nombre de tours']
        time_control = serialized_tournament['Controle du temps']
        description = serialized_tournament['Description']
        players_ids = serialized_tournament["Joueurs_id"]
        list_of_tours = serialized_tournament["Tours"]
        tournament_id = serialized_tournament["Id du tournoi"]

        return Tournament(tournament_name,
                          location,
                          tournament_date,
                          number_of_tours,
                          time_control,
                          description,
                          players_ids,
                          list_of_tours,
                          tournament_id
                          )
#Il manque une partie du programme 

tournament_id = tournament_database.insert(tournament.serialized())
tournament_database.update({"Id du tournoi": tournament_id}, doc_ids=[tournament_id])

class Match_1(self, P1=Jona, P5=Clark):
    TitreMatch = "P1 contre P5"
    if Jona.score > Clark.score:
       print("Jona Wins and Clark Loses")
       Jona.game_wins = 1 
       Clark.game_loses = 0 #(est-ce que je peux créer une variable tel que random choisi entre 1, 0,5 et 0)
    elif Jona.score < Clark.score:    
       print("Clark wins and Jona loses")
       Jona.game_loses = 0
       Clark.game_wins = 1
    else: Jona.score == Clark.score
    print("Jona and Clark make a draw")
    Jona.game_draw = 0.5
    Clark.game_draw = 0.5 