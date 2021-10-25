from tinydb import TinyDB

player_database = TinyDB('models_players.json')

class Player:
    def __init__(self,first_name = None,
                       last_name = None,
                       birthdate = None,
                          gender = None,  
                         ranking = None,
                           score = 0,
                       player_id = 0
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.player_id = player_id

class Game: #Non ici il faut une méthode game
    def __init__(self, game_wins=1,game_loses=0, game_draw=0.5):
        self.game_wins = game_wins
        self.game_loses = game_loses
        self.game_draw = game_draw
        
#Voici des instances de la classe Player
Jona = Player('Jonathan', 'BUISSON', '09.11.1985', 'Man' ,'700','90','1')
print(Jona.last_name)
Micha = Player('Michael','DWIGHT','01.01.1980','Man','700', '50','2')
print(Micha.score)
Maria = Player('Maria','PEREZ','12.08.1982','Woman','700','20','3')
print(Maria.gender)
Ivana = Player('Ivana','SIDOROV','15.12.1995','Woman','800','40','4')
print(Ivana.ranking)
Clark = Player('Clark','KENT','26.04.1977','Man','1000','100','5')
print(Clark.birthdate)
Zata = Player('Zatana','COOPER','20.03.1990','Woman','900','80','6')
print(Zata.first_name)
Martin = Player('Martin','DUPOND','22.09.1975','Man','990','90','7')
print(Martin.ranking)
Xena = Player('Xena','GABRIEL','29.03.1970','Woman','985','70','8')
print(Xena.player_id)

"""Lorsqu'on remplit un formulaire ou qu'on se présente formellement en anglais,
on donne toujours son prénom puis son nom à l'inverse du français"""
def serialized(self):
    player_infos = {}
    player_infos['Prenom'] = self.first_name
    player_infos['Nom'] = self.last_name
    player_infos['Date_de_naissance'] = self.birthdate
    player_infos['Sexe_ou_Genre'] = self.gender
    player_infos['Classement'] = self.ranking
    player_infos['Score'] = self.score
    player_infos['Id du joueur'] = self.player_id
    return player_infos

def unserialized(self, serialized_player):
    first_name = serialized_player['Prenom']
    last_name = serialized_player['Nom']
    birthdate = serialized_player['Date_de_naissance']
    gender = serialized_player['Sexe_ou_Genre']
    ranking = serialized_player['Classement']
    tournament_score = serialized_player['Score']
    player_id = serialized_player['Id_du_joueur']
    return Player(first_name,
                   last_name,
                   birthdate,
                     gender,
                    ranking,
                      score,
                  player_id
                 )

def __str__(self):
    return f"first_name:{self.first_name} last_name:{self.last_name}, classement: {self.ranking}"

#def __repr__(self):
   # return f"first_name:{self.first_name} last_name:{self.last_name}, classement: {self.ranking}"
