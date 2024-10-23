# Write your solution here


def hockey_stats():
    import json
    file = input("file name: ")

    with open(file) as f:
        data = json.load(f)

    print(f"read the data of {len(data)} players")
    print()
    print("commands:\n0 quit\n1 search for player\n2 teams\n3 countries \n4 players in team\n5 players from country\n6 most points\n7 most goals")
    print()

    def search_player(name): # com == 1
        for player in data:
            name = player['name']
            team = player['team']
            goals = player['goals']
            assists = player['assists']
            points = goals + assists
        # Print the output in the desired format
        if name:
            print(f"{name:<20} {team:>3} {goals:>3} + {assists:>2} = {points:>3}")       
        #print(f"{name:<20} {team:>3} {goals:>2} + {assists:>2} = {points:>3}")
        else: print("NO such player")

    def print_teams(): # com == 2  
        teams = [data[i]['team'] for i in range(len(data))]

        for team in sorted(set(teams)):
            print(team)

    def print_coutries(): # com == 3
        # ctr = []
        # for i in range(len(data)):
        #     ctr.append(data[i]["nationality"])
        
        cntrs = [data[i]["nationality"] for i in range(len(data))]
        for country in sorted(set(cntrs)):
            print(country)

    def player_in_team(): # com == 4
            team_in = input("team: ")
            data.sort(key=lambda x: x['goals'] + x['assists'], reverse=True)

            for player in data:
                name = player['name']
                team = player['team']
                goals = player['goals']
                assists = player['assists']
                points = goals + assists

                # Print the output in the desired format
                if team == team_in:
                    print(f"{name:<20} {team:>3} {goals:>3} + {assists:>2} = {points:>3}")

    def players_from_country(): # com == 5
        cty = input("country: ")
        data.sort(key=lambda x: x['goals'] + x['assists'], reverse=True)

        for player in data:
            name = player['name']
            team = player['team']
            goals = player['goals']
            assists = player['assists']
            nat = player["nationality"]
            points = goals + assists

            if nat == cty:
                print(f"{name:<20} {team:>3} {goals:>3} + {assists:>2} = {points:>3}")

    def most_points(): # com == 6
            nr = int(input('how many: '))
            # sort by points
            data.sort(key=lambda x: x['goals'] + x['assists'], reverse=True)

            for player in data[:nr]:
                name = player['name']
                team = player['team']
                goals = player['goals']
                assists = player['assists']
                nat = player["nationality"]
                points = goals + assists

                print(f"{name:<20} {team:>3} {goals:>3} + {assists:>2} = {points:>3}")

    def most_goals(): # com == 7
            nr = int(input("how many: "))
            # so you can sort by first criteria and then second one just put it in the pracets "()"
            data.sort(key=lambda x: (-x['goals'], x['games']))

            for player in data[:nr]:
                name = player['name']
                team = player['team']
                goals = player['goals']
                assists = player['assists']
                nat = player["nationality"]
                points = goals + assists

                print(f"{name:<20} {team:>3} {goals:>3} + {assists:>2} = {points:>3}")

    while True:
        com = input("command: ")
        if com == '1':
            # check the name in lst, print out name, counry , goals and stuff
            n = input("name: ")        
            search_player(n)

        if com == "2":
            # print all teams
            print_teams()
            
        if com == "3":
            # print all countries
           print_coutries()

        if com  == "4":
          player_in_team()

        if com == '5':
          players_from_country()  

        if com == '6':
          most_points()  

        if com == "7":
          most_goals()  

        if com == "0":
            break
    


hockey_stats()