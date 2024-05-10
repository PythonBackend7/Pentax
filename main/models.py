from django.db import models


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class About(TimeStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='about')

    def __str__(self):
        return self.title


class Happy_clients(TimeStamp):
    name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    image = models.ImageField(upload_to='clients')
    description = models.TextField()

    def __str__(self):
        return self.name


class Service(TimeStamp):
    icon = models.ImageField(upload_to='service')
    title = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class Category(TimeStamp):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Project(TimeStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='projects')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Artickle(TimeStamp):
    pass


class Price(TimeStamp):
    pass


class Contact(TimeStamp):
    pass
