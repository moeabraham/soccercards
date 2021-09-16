from django.forms import ModelForm
from .models import Fixture

class FixtureForm(ModelForm):
    class Meta:
        model = Fixture
        fields= ['opp', 'championship', 'date']