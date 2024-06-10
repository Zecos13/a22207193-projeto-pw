from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Comment by {self.author_name} on {self.article.title}"


class Rating(models.Model):
    article_rated = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()

    def __str__(self):
        return f"Rating {self.rating} on {self.article_rated.title}"