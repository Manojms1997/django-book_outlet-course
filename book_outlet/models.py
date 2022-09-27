from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(null = True, max_length=100)
    is_best_selling_book = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    def save(self, *args,** kwargs):
        self.slug = slugify(self.title)
        super().save()


    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"