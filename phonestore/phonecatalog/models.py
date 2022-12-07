from django.db import models

# Create your models here.


class phone (models.model):
    phone_name = models.Charfield(max_length=50)
    make = model.Charfield(max_length=50)


def __str__(self):
    return f'{self.make}{self.phone_name}'

    # self is used to refer to the current object
    # the return statement  the f ensures the output is in string form


m
