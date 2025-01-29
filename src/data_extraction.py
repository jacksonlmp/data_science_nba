from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
import pandas as pd
import os
import time

team_conferences = {
    1610612737: 'East',  # Atlanta Hawks
    1610612738: 'East',  # Boston Celtics
    1610612739: 'East',  # Cleveland Cavaliers
    1610612740: 'West',  # New Orleans Pelicans
    1610612741: 'East',  # Chicago Bulls
    1610612742: 'West',  # Dallas Mavericks
    1610612743: 'West',  # Denver Nuggets
    1610612744: 'West',  # Golden State Warriors
    1610612745: 'West',  # Houston Rockets
    1610612746: 'West',  # Los Angeles Clippers
    1610612747: 'West',  # Los Angeles Lakers
    1610612748: 'East',  # Miami Heat
    1610612749: 'East',  # Milwaukee Bucks
    1610612750: 'West',  # Minnesota Timberwolves
    1610612751: 'East',  # Brooklyn Nets
    1610612752: 'East',  # New York Knicks
    1610612753: 'East',  # Orlando Magic
    1610612754: 'East',  # Indiana Pacers
    1610612755: 'East',  # Philadelphia 76ers
    1610612756: 'West',  # Phoenix Suns
    1610612757: 'West',  # Portland Trail Blazers
    1610612758: 'West',  # Sacramento Kings
    1610612759: 'West',  # San Antonio Spurs
    1610612760: 'West',  # Oklahoma City Thunder
    1610612761: 'East',  # Toronto Raptors
    1610612762: 'West',  # Utah Jazz
    1610612763: 'West',  # Memphis Grizzlies
    1610612764: 'East',  # Washington Wizards
    1610612765: 'East',  # Detroit Pistons
    1610612766: 'East',  # Charlotte Hornets
}

def get_nba_teams():
    return teams.get_teams()

def group_teams_by_conference(nba_teams):
    eastern_conference = []
    western_conference = []

    for team in nba_teams:
        team_id = team['id']
        conference = team_conferences.get(team_id)
        if conference == 'East':
            eastern_conference.append(team)
        elif conference == 'West':
            western_conference.append(team)

    return eastern_conference, western_conference

def save_teams_to_csv(eastern_conference, western_conference):
    eastern_df = pd.DataFrame(eastern_conference)
    western_df = pd.DataFrame(western_conference)

    if not os.path.exists('data/processed'):
        os.makedirs('data/processed')

    eastern_df.to_csv('data/processed/eastern_conference_teams.csv', index=False)
    western_df.to_csv('data/processed/western_conference_teams.csv', index=False)

def get_team_games(team_id):
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    games = gamefinder.get_data_frames()[0]
    return games

def save_games_to_csv(team_id, games, team_name):
    if not os.path.exists('data/raw'):
        os.makedirs('data/raw')

    games.to_csv(f'data/raw/{team_name}_games.csv', index=False)

# Lista de nomes dos jogadores
jogadores = [
    "Jayson Tatum", "Derrick White", "Jaylen Brown", "Al Horford", "Marcus Smart",
    "Robert Williams III", "Malcolm Brogdon", "Sam Hauser", "Luke Kornet", 
    "Payton Pritchard", "Grant Williams", "Juwan Morgan", "Matisse Thybulle"
]

# Função para buscar dados de um jogador
def buscar_dados_jogador(nome):
    jogador = players.find_players_by_full_name(nome)
    if jogador:
        jogador_id = jogador[0]['id']
        info = commonplayerinfo.CommonPlayerInfo(player_id=jogador_id).get_dict()
        dados = info['resultSets'][0]['rowSet'][0]
        return {
            "Nome": nome,
            "Altura": dados[10],  # Altura (em metros)
            "Peso": dados[11],  # Peso (em kg)
            "Idade": dados[6],  # Idade
            "Experiência": dados[12],  # Anos na NBA
            "Posição": dados[14],  # Posição
            "Universidade": dados[8],  # Universidade
            "Salário": dados[17] if len(dados) > 17 else 0  # Salário atual
        }
    return None

# Criar DataFrame com os dados dos jogadores
dados_jogadores = []
for nome in jogadores:
    print(f"Buscando dados para: {nome}")
    dados = buscar_dados_jogador(nome)
    if dados:
        dados_jogadores.append(dados)
    else:
        print(f"Não foi possível encontrar dados para {nome}")
    time.sleep(1)  # Adiciona um atraso para evitar problemas com a API

# Criar e salvar o arquivo CSV
df = pd.DataFrame(dados_jogadores)
df.to_csv("data/players.csv", index=False)
print("Arquivo players.csv criado com sucesso!")

def main():
    nba_teams = get_nba_teams()

    eastern_conference, western_conference = group_teams_by_conference(nba_teams)

    print("Conferência Leste:")
    for team in eastern_conference:
        print(f"ID: {team['id']}, Nome: {team['full_name']}")

    print("\nConferência Oeste:")
    for team in western_conference:
        print(f"ID: {team['id']}, Nome: {team['full_name']}")

    save_teams_to_csv(eastern_conference, western_conference)

    for team in nba_teams:
        team_id = team['id']
        team_name = team['full_name'].replace(' ', '_')
        games = get_team_games(team_id)
        save_games_to_csv(team_id, games, team_name)
        print(f"Dados de jogos do {team['full_name']} salvos em 'data/raw/{team_name}_games.csv'")

if __name__ == "__main__":
    main()
