from django.db import models

# Create your models here.
class Memory(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    tags = models.Charfield(max_length=150) # tag-refy, odseparowane przecinkami
    body = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True) # image-refy, odseparowane przecinkami
    links = models.TextField(blank=True, null=True)
    sharedwith = models.TextField(blank=True, null=True)

    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title

    #Ta funkcja ogranicza długość tekstu na stronie wpisów, żeby nie było zbyt rozlegle i każdy mógł sobie wybrać...
    def summary(self):
        return self.body[:110]

    #Funkcja formatująca datę w ludzki sposób...
    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')

class MemoryImage(models.Model):
    imageref = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.imageref

class MemoryTag(models.Model):
    tagref = models.CharField(max_length=100)
    tagname = models.CharField(max_length=100)

    def __str__(self):
        return self.tagref
