from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)


class Category(models.Model):
    title = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
    
