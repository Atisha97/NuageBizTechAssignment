from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=30, default="qwerty")
    # author = models.ForeignKey('Author', related_name='articles', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


# class Author(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name