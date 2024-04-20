from .models import Judge
def allocate_teams_to_judges(judges_count, teams, judge_mode):
    filtered_judges = []  # Initialize an empty list to hold filtered judges
    allocated_teams = {}  # Initialize an empty dictionary for allocated teams

    # Logic to filter judges based on mode
    if judge_mode == 'online':
        filtered_judges = Judge.objects.filter(mode='online')[:judges_count]
    elif judge_mode == 'offline':
        filtered_judges = Judge.objects.filter(mode='offline')[:judges_count]

    # Initialize allocated teams for each judge
    for judge in filtered_judges:
        allocated_teams[judge.judge_name] = []

    # Allocate teams to judges
    for index, team in enumerate(teams):
        judge_index = index % len(filtered_judges)
        judge_name = filtered_judges[judge_index].judge_name
        allocated_teams[judge_name].append(team)

    return allocated_teams
