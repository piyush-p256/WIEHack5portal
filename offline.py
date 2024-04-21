import os
import django
import openpyxl

# Modify this line to point to your Django project's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Team

def import_teams_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        email, password, team_no, round_no, mode, team_name, team_leader = row
        team = Team.objects.create(
            email=email,
            password=password,
            team_no=team_no,
            round_no=round_no,
            mode=mode,
            team_name=team_name,
            team_leader=team_leader
        )
        print(f"Team {team.team_no} created.")

if __name__ == "__main__":
    # Replace 'your_file.xlsx' with the actual Excel file path
    file_path = 'offline.xlsx'
    import_teams_from_excel(file_path)
