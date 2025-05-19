teams={
    'Iran':      {'wins':0, 'loses':0,'draws':0, 'goal_difference':0, 'points':0 },
    'Portugal':  {'wins':0, 'loses':0,'draws':0, 'goal_difference':0, 'points':0 },
    'Spain':     {'wins':0, 'loses':0,'draws':0, 'goal_difference':0, 'points':0 },
    'Morocco':   {'wins':0, 'loses':0,'draws':0, 'goal_difference':0, 'points':0 }
}
results=[]
matches=[
    ('Iran','Spain'),
    ('Iran','Portugal'),
    ('Iran','Morocco'),
    ('Spain','Portugal'),
    ('Spain','Morocco'),
    ('Portugal','Morocco' )
]

for match in matches :
    result=input()
    goals_for, goals_against=map(int,result.split('-'))
    results.append((goals_for,goals_against))

def update_team_states(team_name,goals_for,goals_against):
    team=teams[team_name]
    if goals_for>goals_against:
        team['wins']+=1 
        team['points']+=3 
    elif goals_for<goals_against:
        team['loses']+=1 
    else:
        team['draws']+=1 
        team['points']+=1 
    team['goal_difference']+=goals_for-goals_against
for i , (team1_goals,team2_gaols) in enumerate(results):
    match=matches[i]
    update_team_states(match[0],team1_goals, team2_gaols )
    update_team_states(match[1],team2_gaols , team1_goals)
    sorted_teams=sorted(teams.items() , key=lambda x: (-x[1]['points'], -x[1]['wins'],x[0]))
    
for team_name, team_state in sorted_teams:
    print(f'{team_name}  wins:{team_state['wins']} , loses:{team_state['loses']} , draws:{team_state['draws']} , goal_difference:{team_state['goal_difference']} , points:{team_state['points']}')