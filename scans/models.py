from django.db import models
from django.forms import ModelForm

# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=200)
    filezip = models.FileField(upload_to="./media")
    pub_date = models.DateTimeField('date published')
class File(models.Model):
    App = models.ForeignKey(App)
    path = models.CharField(max_length=2000)
    scanresults = models.TextField()

    
class AppForm(ModelForm):
    class Meta:
        model = App
        fields = ['name', 'filezip']
