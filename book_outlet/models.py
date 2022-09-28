from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def __str__(self) -> str:
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    # author = models.CharField(null = True, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_best_selling_book = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    def save(self, *args,** kwargs):
        self.slug = slugify(self.title)
        super().save()


    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"

