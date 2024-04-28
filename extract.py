import os
import django
import pandas as pd

# Set the Django settings module in your script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Initialize Django
django.setup()

# Now you can import your models
from myapp.models import Round2

# Get data from Round3 model
round2_data = Round2.objects.all().values()

# Convert queryset to DataFrame
df = pd.DataFrame(list(round2_data))

# Define the Excel file path
excel_file_path = 'round2_data.xlsx'

# Write DataFrame to Excel
df.to_excel(excel_file_path, index=False)

print(f"Data exported to {excel_file_path}")
