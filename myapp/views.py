from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .utils import allocate_teams_to_judges
from .models import Team, Round1, Round2, Round3, UniversalSettings, Judge
from .forms import Round1Form, Round3UploadForm, Round2UploadForm
from django.conf import settings
from django.db.models import Q 



#login
def login(request):
    current_round = UniversalSettings.objects.first().current_round
    error_message = None
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            team = Team.objects.get(email=email, password=password)
            if team.round_no == current_round:
                request.session['team_email'] = team.email
                if team.round_no == 1:
                    return redirect('round1')
                elif team.round_no == 2:
                    return redirect('round2')
                elif team.round_no == 3:
                    return redirect('round3')
                elif team.round_no == 4:
                    return redirect('round4')
            else:
                return redirect('not_selected')
        except Team.DoesNotExist:
            error_message = 'Invalid credentials!'
    
    context = {'error_message': error_message}
    return render(request, 'login.html', context)

def round1(request):
    team_email = request.session.get('team_email')  # Retrieve team_email from session
    
    # Pass team_email to the context
    context = {'team_email': team_email}
    return render(request, 'round1.html', context)

def round2(request):
    team_email = request.session.get('team_email')  # Retrieve team_email from session
    
    # Pass team_email to the context
    context = {'team_email': team_email}
    return render(request, 'round2.html', context)

def round3(request):
    team_email = request.session.get('team_email')  # Retrieve team_email from session
    
    context = {'team_email': team_email}  # Pass team_email to the context
    return render(request, 'round3.html', context)

from django.shortcuts import render

def round4(request):
    team_email = request.session.get('team_email')  # Retrieve team_email from session
    
    context = {'team_email': team_email}  # Pass team_email to the context
    return render(request, 'round4.html', context)

def not_selected(request):
    team_email = request.session.get('team_email')  # Retrieve team_email from session
    
    context = {'team_email': team_email}  # Pass team_email to the context
    return render(request, 'not_selected.html', context)

def submit1(request):
    return render(request, 'submit1.html')

def success_page(request):
    team_email = request.session.get('team_email')  # Retrieve team_email from session
    
    # Pass team_email to the context
    context = {'team_email': team_email}
    return render(request, 'success.html')


#judge online login logic



def judge_online_login(request):
    error_message = ''  # Initialize error message
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            judge = Judge.objects.get(email=email, password=password)
            current_round = UniversalSettings.objects.first().current_round

            if current_round == 1:
                request.session['judge_name'] = judge.judge_name  # Store judge's name in session
                return redirect('judge_round1')
            elif current_round == 2:
                request.session['judge_name'] = judge.judge_name  # Store judge's name in session
                return redirect('judge_round2')
            elif current_round == 3:
                request.session['judge_name'] = judge.judge_name  # Store judge's name in session
                return redirect('judge_round3')
            else:
                return redirect('invalid_round')  # Add this view for custom handling

        except Judge.DoesNotExist:
            error_message = 'Invalid credentials!'
    
    return render(request, 'on-judge-login.html', {'error': error_message})



#judge round1
def judge_round1(request):
    return render(request, 'judge-round1.html')

def judge_round2(request):
    return render(request, 'judge-round2.html')

def judge_round3(request):
    return render(request, 'judge-round3.html')

def offline_judge_round1(request):
    return render(request, 'offline-judge-round1.html')

def offline_judge_round2(request):
    return render(request, 'offline-judge-round2.html')

def offline_judge_round3(request):
    return render(request, 'offline-judge-round3.html')

#off judge login logic
def judge_offline_login(request):
    error_message = ''  # Initialize error message
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            judge = Judge.objects.get(email=email, password=password)
            current_round = UniversalSettings.objects.first().current_round

            if current_round == 1:
                request.session['judge_name'] = judge.judge_name  # Store judge's name in session
                return redirect('offline_judge_round1')
            elif current_round == 2:
                request.session['judge_name'] = judge.judge_name  # Store judge's name in session
                return redirect('offline_judge_round2')
            elif current_round == 3:
                request.session['judge_name'] = judge.judge_name  # Store judge's name in session
                return redirect('offline_judge_round3')
            else:
                return redirect('invalid_round')  # Add this view for custom handling

        except Judge.DoesNotExist:
            error_message = 'Invalid credentials!'
    
    return render(request, 'off-judge-login.html', {'error': error_message})
#round 1 upload form 



#allocate judges




#online round
def judge_round1(request):
    judge_name = request.session.get('judge_name')  # Retrieve judge_name from session
    judges_count = len(Judge.objects.filter(mode='online'))  # Count online judges
    teams = Round1.objects.filter(mode='online')  # Filter Round1 teams with mode='online'

    allocated_teams = allocate_teams_to_judges(judges_count, teams, judge_mode='online')

    context = {
        'allocated_teams': allocated_teams,
        'judge_name': judge_name  # Pass judge_name to the context
    }
    return render(request, 'judge-round1.html', context)



def judge_round2(request):
    judge_name = request.session.get('judge_name')  # Retrieve judge_name from session
    teams = Round2.objects.order_by('team_no')  # Fetch all Round2 teams sorted by team number

    context = {
        'teams': teams,
        'judge_name': judge_name
    }
    return render(request, 'judge-round2.html', context)




#online 3
def judge_round3(request):
    judge_name = request.session.get('judge_name')  # Retrieve judge_name from session
    teams = Round3.objects.order_by('team_no')  # Get all Round3 teams sorted by team number

    context = {
        'teams': teams,
        'judge_name': judge_name 
    }
    return render(request, 'judge-round3.html', context)

#allcate to offline round1


#off judge round1
def offline_judge_round1(request):
    judge_name = request.session.get('judge_name')  # Retrieve judge_name from session
    judges_count = len(Judge.objects.filter(mode='offline'))  # Count offline judges
    teams = Round1.objects.filter(mode='offline')  # Filter Round1 teams with mode='offline'

    allocated_teams = allocate_teams_to_judges(judges_count, teams, judge_mode='offline')

    context = {
        'allocated_teams': allocated_teams,
        'judge_name': judge_name  # Pass judge_name to the context
    }
    return render(request, 'offline-judge-round1.html', context)

#judge round2
def offline_judge_round2(request):
    judge_name = request.session.get('judge_name')  # Retrieve judge_name from session
    teams = Round2.objects.order_by('team_no')  # Get all Round3 teams sorted by team number

    context = {
        'teams': teams,
        'judge_name': judge_name 
    }
    return render(request, 'offline-judge-round2.html', context)


def offline_judge_round3(request):
    judge_name = request.session.get('judge_name')  # Retrieve judge_name from session
    teams = Round3.objects.order_by('team_no')  # Get all Round3 teams sorted by team number

    context = {
        'teams': teams,
        'judge_name': judge_name 
    }
    return render(request, 'offline-judge-round3.html', context)


#round1upload

#round1upload
def round1_upload(request):
    team_email = request.session.get('team_email')  # Retrieve team_email from session
    universal_settings = UniversalSettings.objects.first()  # Get the UniversalSettings instance

    if universal_settings and universal_settings.upload:  # Check if submissions are allowed
        if request.method == 'POST':
            form = Round1Form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success_page')  # Redirect to success page or another URL
        else:
            form = Round1Form()
    
        context = {'form': form, 'team_email': team_email}  # Pass team_email to the context
        return render(request, 'round1-upload.html', context)
    else:
        return render(request, 'submission_not_started.html')


#round2upload

def round2_upload(request):
    team_email = request.session.get('team_email')  # Retrieve team_email from session
    universal_settings = UniversalSettings.objects.first()  # Get the UniversalSettings instance

    if universal_settings and universal_settings.upload:  # Check if submissions are allowed
        if request.method == 'POST':
            form = Round2UploadForm(request.POST)
            if form.is_valid():
                team_no = form.cleaned_data['team_no']
                email = form.cleaned_data['team_email']
                
                # Check if team_no and email belong to the same team in the Team model
                try:
                    team = Team.objects.get(team_no=team_no, email=email)
                except Team.DoesNotExist:
                    # Team not found for the given team_no and email
                    form.add_error(None, 'Invalid team details!')
                    context = {'form': form, 'team_email': team_email}
                    return render(request, 'round2-upload.html', context)
                
                # Save the form data
                form.save()
                return redirect('success_page')  # Redirect to success page after successful form submission
        else:
            form = Round2UploadForm()
    
        context = {'form': form, 'team_email': team_email}  # Pass team_email to the context
        return render(request, 'round2-upload.html', context)
    else:
        return render(request, 'submission_not_started.html')


def round3_upload(request):
    team_email = request.session.get('team_email')  # Retrieve team_email from session
    universal_settings = UniversalSettings.objects.first()  # Get the UniversalSettings instance

    if universal_settings and universal_settings.upload:  # Check if submissions are allowed
        if request.method == 'POST':
            form = Round3UploadForm(request.POST)
            if form.is_valid():
                team_no = form.cleaned_data['team_no']
                email = form.cleaned_data['team_email']
                
                # Check if team_no and email belong to the same team in the Team model
                try:
                    team = Team.objects.get(team_no=team_no, email=email)
                except Team.DoesNotExist:
                    # Team not found for the given team_no and email
                    form.add_error(None, 'Invalid team details!')
                    context = {'form': form, 'team_email': team_email}
                    return render(request, 'round3-upload.html', context)
                
                # Save the form data
                form.save()
                return redirect('success_page')  # Redirect to success page after successful form submission
        else:
            form = Round3UploadForm()
    
        context = {'form': form, 'team_email': team_email}  # Pass team_email to the context
        return render(request, 'round3-upload.html', context)
    else:
        return render(request, 'submission_not_started.html')
