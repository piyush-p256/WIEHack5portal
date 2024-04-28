import pandas as pd
from myapp.models import Round3

def export_round3_data_to_excel(filepath):
    # Query all objects from Round3 model
    round3_data = Round3.objects.all()

    # Create a DataFrame from the queryset
    data_list = []
    for item in round3_data:
        data_list.append({
            'team_email': item.team_email,
            'team_no': item.team_no,
            'team_name': item.team_name,
            'mode': item.mode,
            'member_name': item.member_name,
            'member2': item.member2,
            'member3': item.member3,
            'member4': item.member4,
            'youtube_link3': item.youtube_link3,
            'github_link3': item.github_link3,
            'ppt3_link': item.ppt3_link,
        })
    
    df = pd.DataFrame(data_list)

    # Write DataFrame to Excel
    df.to_excel(filepath, index=False)
    print(f"Round3 data exported to {filepath}")

if __name__ == "__main__":
    output_file = "round3_data.xlsx"
    export_round3_data_to_excel(output_file)
