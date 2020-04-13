import basketball_team_stats.constants as stats


def teams_dict():
    return dict((index, team) for index, team in enumerate(stats.TEAMS))

def players_dict():
    players = dict((index, player) for index, player in enumerate(stats.PLAYERS))
    for key, player in players.items():
        player_guardian = player['guardians']
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
        if player.get('experience') == 'YES':
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    players_list = [item for pair in zip(experienced_players, inexperienced_players +[0]) for item in pair][:-1]
    team1 = list(players_list)[:players_list_length//teams_list_length]
    team2 = list(players_list)[len(team1) : len(team1) * 2]
    team3 = list(players_list)[len(team2) * 2 - 1:]
    return team1, team2, team3
     
def display_stats():
    print("\n" + "BASKETBALL TEAM STATS TOOL" + "\n")
    print("-------- MENU -------" + "\n")
    team1, team2, team3 = distribute_players(players=players_dict().items(), teams=teams_dict().items())
    
    try:
        experienced = ""
        experienced_count=0
        inexperienced = ""
        inexperienced_count=0
        show_teams = int(input("Here are your choices:\n 1) Display Team Stats \n 2) Quit\n\nEnter an option greater than one: "))
        
        if show_teams == 1:
            team_list = list((f'{index}) {team_value}') for index, team_value in enumerate(teams_dict().values(), 1))
            print("\nWhich teams stats would you like to view? ")
            teams = int(input( f"\n {team_list[0]} \n {team_list[1]} \n {team_list[2]} \n \nEnter an option greater than one: "))
            if teams == 1:
                print("\nTeam: Panthers Stats")
                height_list = []
                guardian_list = []
                player_list = []
                print("-" * 30)
                print(f'Total players: {len(team1)} \n')
                print("Players on Team: \n")
                for value in team1:
                    player = value['name']
                    player_list.append(player)
                    height_raw = value['height']
                    height = height_raw.split(" ")
                    height_list.append(int(height[0]))
                    height_sum = sum(height_list)
                    guardian = value['guardians']
                    if len(guardian) > 2:
                        guardian_list.append(guardian)                        
                    else:
                        guardian_list.append(guardian[0])
                        guardian_list.append(guardian[1])
                    if value['experience'] == "YES":
                        experienced_count+=1
                    elif value['experience'] == "NO":
                        inexperienced_count+=1
                print(", ".join(player_list))
                print("\n\n-------Additional Stats-------")
                print("\nGuardians: ", ", ".join(guardian_list))
                print(f'\n \nAverage height for Team 1: {round(height_sum/len(team1))} inches')
                experienced = experienced_count
                inexperienced = inexperienced_count
                print(f'\nExperienced players: {experienced}')
                print(f'Inexperienced players: {inexperienced}')
            if teams == 2:
                print("\nTeam: Bandits Stats")
                height_list = []
                guardian_list = []
                player_list = []
                print("-" * 30)
                print(f'Total players: {len(team2)} \n')
                print("Players on Team: \n")
                for value in team2:
                    player = value['name']
                    player_list.append(player)
                    height_raw = value['height']
                    height = height_raw.split(" ")
                    height_list.append(int(height[0]))
                    height_sum = sum(height_list)
                    guardian = value['guardians']
                    if len(guardian) > 2:
                        guardian_list.append(guardian)                        
                    else:
                        guardian_list.append(guardian[0])
                        guardian_list.append(guardian[1])
                    if value['experience'] == "YES":
                        experienced_count+=1
                    elif value['experience'] == "NO":
                        inexperienced_count+=1
                print(", ".join(player_list))
                print("\n\n-------Additional Stats-------")
                print("\nGuardians: ", ", ".join(guardian_list))
                print(f'\n \nAverage height for Team 2: {round(height_sum/len(team2))} inches')
                experienced = experienced_count
                inexperienced = inexperienced_count
                print(f'\nExperienced players: {experienced}')
                print(f'Inexperienced players: {inexperienced}')
            if teams == 3:
                print("\nTeam: Warriors Stats")
                height_list = []
                guardian_list = []
                player_list = []
                print("-" * 30)
                print(f'Total players: {len(team3)} \n')
                print("Players on Team: \n")
                for value in team3:
                    player = value['name']
                    player_list.append(player)
                    height_raw = value['height']
                    height = height_raw.split(" ")
                    height_list.append(int(height[0]))
                    height_sum = sum(height_list)
                    guardian = value['guardians']
                    if len(guardian) > 2:
                        guardian_list.append(guardian)                        
                    else:
                        guardian_list.append(guardian[0])
                        guardian_list.append(guardian[1])
                    if value['experience'] == "YES":
                        experienced_count+=1
                    elif value['experience'] == "NO":
                        inexperienced_count+=1
                print(", ".join(player_list))
                print("\n\n-------Additional Stats-------")
                print("\nGuardians: ", ", ".join(guardian_list))
                print(f'\n \nAverage height for Team 3: {round(height_sum/len(team3))} inches')
                experienced = experienced_count
                inexperienced = inexperienced_count
                print(f'\nExperienced players: {experienced}')
                print(f'Inexperienced players: {inexperienced}')
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