from django.db import models


class Developer(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    work = models.CharField(max_length=20)
    image = models.ImageField(upload_to='Developer/%m/%d')

    def __str__(self):
        return f'{self.name} | {self.work}'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name



