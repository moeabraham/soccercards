from django.db import models
from django.urls import reverse
from image_cropping import ImageRatioField

# Create your models here.


CHAMPIONSHIPS = (
    ('L', 'League Game'),
    ('C', 'Cup Game'),
    ('E', 'European Game'),

)




class Card(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    age = models.IntegerField()
    # add color and league to card

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cards_detail', kwargs={'card_id': self.id})

        


class Team(models.Model):
    name = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return f"{self.name}  on {self.league}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'team_id' : self.id})


# class Photo(models.Model):
#     name=models.CharField(max_length=50)
#     image = models.ImageField(blank=True, upload_to='uploaded_images')
#     cropping = ImageRatioField('image', '430x360')



    def __str__(self):
        return f'photo for team_id:{self.team_id} @ {self.url}'





class Fixture(models.Model):
    class Meta:
        ordering=['date']



    date = models.DateField()
    opp = models.CharField(max_length=100)
    championship = models.CharField(
        max_length=1,
        choices = CHAMPIONSHIPS,
        default=CHAMPIONSHIPS[0][0]
    )

    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_championship_display()} on {self.date} against {self.opp}"



    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f'photo for team_id:{self.team_id} @ {self.url}'


    