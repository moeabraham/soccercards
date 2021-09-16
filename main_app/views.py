from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from .models import Card
from .models import Team, Photo
from .forms import FixtureForm
from .forms import *
import uuid
import boto3





# check this again
from django.http.response import HttpResponse
from django.http import HttpResponse

import boto3 
import uuid
S3_BASE_URL='https://s3-us-east-2.amazonaws.com/'
BUCKET='soccercards'
# # temporary cards class for testing purposses, django is next

# class Card:
#     def __init__(self, name, nationality, position, age):
#         self.name = name
#         self.nationality = nationality
#         self.position = position
#         self.age = age
# cards= [
#     Card('Zidane', 'french', 'middfield attacker', 34),
#     Card('Ronaldinho', 'brazilian', 'middfield attacker', 28),
#     Card('Roberto Baggio', 'italian', ' stricker', 39),
# ]


# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('abbbbaaaooot')
    return render(request, 'about.html')

def teams_index(request):
    teams = Team.objects.all()
    return render(request, 'teams/index.html', {'teams' : teams})

def add_fixture(request, team_id):
    form = FixtureForm(request.POST)
    if form.is_valid():
        new_fixture = form.save(commit=False)
        new_fixture.team_id = team_id
        new_fixture.save()
    return redirect('detail', team_id=team_id)

def add_photo(request, team_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, team_id = team_id)
            photo.save()

        except Exception as e :
            print('An error occured uploading files to s3')
            print(e)
    return redirect('teams_detail', team_id = team_id)

    

def assoc_card(request, team_id, card_id):
    Team.objects.get(id=team_id).cards.add(card_id)
    return redirect('teams_detail', team_id=team_id)


def teams_detail(request, team_id):
    team = Team.objects.get(id=team_id)
    #get the cards that the team does not have
    cards_teams_doesnt_have = Card.objects.exclude(id__in = team.cards.all().values_list('id'))
    fixture_form = FixtureForm()
    return render(request, 'teams/detail.html', {
        #pass the team and add_fixture_form a context
        'team': team,
        'fixture_form' : fixture_form,
        #add cards to be displayed
        'cards': cards_teams_doesnt_have

    })
# def crop(request, team_id):
#     team = Team.objects.get(id=team_id)
#     return render(request, 'teams/crop.html', {'team':team})



class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'league']
    success_url = '/teams/'

class TeamUpdate(UpdateView):
    model = Team
    fields = ['name', 'league']

class TeamDelete(DeleteView):
    model = Team
    success_url = '/teams'

def cards_index(request):
    cards = Card.objects.all().order_by('-age')
    return render(request, 'cards/index.html', {'cards' : cards} ) # context dictionary in python /context object in jss

def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    return render(request, 'cards/detail.html', {'card' : card} )  #very important how context dictionary works!! why "card" not "cards"!!

class CardCreate(CreateView):
    model = Card
    fields = '__all__'
    success_url = '/cards/'

class CardUpdate(UpdateView):
    model = Card
    fields = ['age', 'position', 'nationality']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'


# def img(request):
#     if request.method == 'POST':

#         form = imgForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save
#             return redirect('/teams')
#     else:
#         form = imgForm()
#         return render(request, 'image_form.html', {'form' : form})
# def success(request):
#     return HttpResponse('successfully uploaded')








# 


# <form class="card-panel" action="{% url 'add_photo' floorplan.id  %}" method="POST" enctype="multipart/form-data">
#     {% csrf_token %}
#     <input type="file" name="photo-file">
#     <br>
#     <br>

#     <input type="submit" value="upload floorplan" class="btn">

# </form>
def success(request):
    pass