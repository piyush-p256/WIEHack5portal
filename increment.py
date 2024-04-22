import openpyxl
from django.core.wsgi import get_wsgi_application
import os

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_wsgi_application()

from myapp.models import Team

def update_round_no_from_excel(file_path):
    # Load the Excel workbook
    wb = openpyxl.load_workbook(file_path)
    
    # Select the active sheet
    sheet = wb.active
    
    # Iterate through rows starting from the second row (assuming first row has headers)
    for row in sheet.iter_rows(min_row=2, values_only=True):
        team_no = row[0]  # Assuming team_no is in the first column
        team = Team.objects.filter(team_no=team_no).first()
        if team:
            team.round_no = 2
            team.save()
            print(f"Updated round_no for team {team_no}")
        else:
            print(f"Team with team_no {team_no} not found")

if __name__ == "__main__":
    # Provide the path to your Excel file
    excel_file_path = "incre.xlsx"
    update_round_no_from_excel(excel_file_path)
