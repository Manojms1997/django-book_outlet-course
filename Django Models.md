# creating model classes in models.py
```python 
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
```

# creating migrations
to create migration
```sh
python manage.py makemigrations
```

to migrate to database
```sh
python manage.py migrate
```

# Inserting data to db using models
We can use django interactive shell to try inserting data to db
```sh
python manage.py shell
```

python shell:
```sh
In [1]: from book_outlet.models import Book

In [2]: harry_potter = Book(title="The Philosopher's Stone", ratin 
   ...: g=5)

In [3]: harry_potter.save()

In [4]: lord_of_the_rings = Book(title="The last king",rating=5)   

In [5]: lord_of_the_rings.save()
```
# get data
```sh
Book.objects.all()
```

# update database
- make the changes to models.py file

run makemigratiions command again
```sh
python manage.py makemigrations
```
run migrate command to reflect these changes in db
```python
python manage.py migrate
```
# updating data in database:
```sh
In [5]: Book.objects.all()[1].is_best_selling_book
Out[5]: False

In [6]: harry_potter = Book.objects.all()[0]

In [7]: lotr = Book.objects.all()[1]

In [8]: harry_potter.author = "J.K.Rowling"

In [9]: harry_potter.is_best_selling_book = True

In [10]: harry_potter.save()

In [11]: Book.objects.all()[0].author
Out[11]: 'J.K.Rowling'
```
# Delete Data
```sh
In [12]: harry_potter.delete()
Out[12]: (1, {'book_outlet.Book': 1})

In [13]: Book.objects.all()
Out[13]: <QuerySet [<Book: The last king (5)>]>
```

# "Create" Data
Instead of initialising a Book object and calling save on it we can use create method to create data 
```python
	Book.objects.create(title="Harry Potter 1",rating=5,author="J.K. Rowling", is_best_selling_book = True)
```
# Querying and Filtering data
To get a single entry use "get()"
```python
In [18]: Book.objects.get(title="Harry Potter 1")
Out[18]: <Book: Harry Potter 1 (5)>
```

To get all entries from db with matching queries
```python
In [20]: Book.objects.filter(rating=5)
Out[20]: <QuerySet [<Book: The last king (5)>, <Book: Harry Potter 
1 (5)>]>
```

# "OR" query
For "A or B" kind of query:

```python
from django.db.models import Q
In [7]: Book.objects.filter(Q(is_best_selling_book=False) | Q(titl 
   ...: e="Harry Potter 1"))
Out[7]: <QuerySet [<Book: The last king (5)>, <Book: Harry Potter 1 (5)>]>
```

# slugify the model data 
models.py:
inside class
```python 
    slug = models.SlugField(default="", null=False, db_index=True)
    
   def save(self, *args,** kwargs):
        self.slug = slugify(self.title)
        super().save()
```
Now whenever we save an entry in db, a column named slug is added with hyphen seperated title
