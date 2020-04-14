import basketball_team_stats.constants as stats


def teams_dict():
    return dict((index, team) for index, team in enumerate(stats.TEAMS))

def players_dict():
    players = dict((index, player) for index, player in enumerate(stats.PLAYERS))
    for key, player in players.items():
        player_guardian = player['guardians']
        height_raw = player['height']
        if height_raw is not None and type(height_raw) == str:
            height_list = height_raw.split(" ")
            height = int(height_list[0])
            player['height'] = height
        if player['experience'] == 'YES':
            player['experience'] = True
        if player.get('experience') == 'NO':
            player['experience'] = False
        if player_guardian is not None:
            if "and" in player_guardian:
                player_guardian_updated = list(player_guardian_names.strip() for player_guardian_names in player_guardian.split("and"))
                player['guardians'] = player_guardian_updated
        else:
            return key, players
    return players
    
def distribute_players(players, teams):
    players_list_length = len(players)
    teams_list_length = len(teams)
    experienced_players = []
    inexperienced_players = []
    for key, player in players:
        if player.get('experience') == True:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    players_list = [item for pair in zip(experienced_players, inexperienced_players +[0]) for item in pair][:-1]
    team1 = list(players_list)[:players_list_length//teams_list_length]
    team2 = list(players_list)[len(team1) : len(team1) * 2]
    team3 = list(players_list)[len(team2) * 2 - 1:]
    return team1, team2, team3

def team_stats(team_number, team_name):
    experienced = ""
    experienced_count=0
    inexperienced = ""
    inexperienced_count=0
    height_list = []
    guardian_list = []
    player_list = []
    print(f"\nTeam: {team_name} Stats")
    print("-" * 30)
    print(f'Total players: {len(team_number)} \n')
    print("Players on Team: \n")
    for value in team_number:
        player = value['name']
        height = value['height']
        player_list.append(player)
        height_list.append(height)
        height_sum = sum(height_list)
        guardian = value['guardians']
        if len(guardian) > 2:
            guardian_list.append(guardian)                        
        else:
            guardian_list.append(guardian[0])
            guardian_list.append(guardian[1])
        if value['experience'] == True:
            experienced_count+=1
        elif value['experience'] == False:
            inexperienced_count+=1
    print(", ".join(player_list))
    print("\n\n-------Additional Stats-------")
    print("\nGuardians: ", ", ".join(guardian_list))
    print(f'\n \nAverage height for Team 1: {round(height_sum/len(team_number))} inches')
    experienced = experienced_count
    inexperienced = inexperienced_count
    print(f'\nExperienced players: {experienced}')
    print(f'Inexperienced players: {inexperienced}')

def display_stats():
    print("\n" + "BASKETBALL TEAM STATS TOOL" + "\n")
    print("-------- MENU -------" + "\n")
    team1, team2, team3 = distribute_players(players=players_dict().items(), teams=teams_dict().items())
    
    try:
        show_teams = int(input("Here are your choices:\n 1) Display Team Stats \n 2) Quit\n\nEnter the number one or two: "))
        if show_teams == 1:
            team_list = list((f'{index}) {team_value}') for index, team_value in enumerate(teams_dict().values(), 1))
            print("\nWhich teams stats would you like to view? ")
            teams = int(input( f"\n {team_list[0]} \n {team_list[1]} \n {team_list[2]} \n \nEnter an option greater than one: "))
            if teams == 1:
                team_stats(team_number=team1, team_name="Panthers")
            if teams == 2:
                team_stats(team_number=team2, team_name="Bandits")
            if teams == 3:
                team_stats(team_number=team3, team_name="Warriors")
            continue_stats = input("\nPress ENTER to continue")
            if continue_stats == "":
                display_stats()
            else:
                print("Thanks for viewing our stats.")
        else:
            print("Thanks for viewing our stats.")
    except ValueError:
        print("-" * 35)
        display_stats()
        

if __name__ == '__main__':
    display_stats()