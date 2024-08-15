from django.db import models


from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class reviews(models.Model):
    title=models.CharField(max_length=100)
    published=models.IntegerField()
    summary=models.TextField()
    points=models.PositiveSmallIntegerField(default=0,validators=[MaxValueValidator(10)])
    chapter=models.PositiveIntegerField(null=True)
    tags=models.TextField(null=True)
    is_complete=models.BooleanField(default=False)
    image=models.ImageField(blank=True)
    #cpk = models.AutoField(primary_key=True)
    #owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='manhwas')

    def __str__(self):
        return f"|| Name : {self.title} ||"

class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    Favorite= models.ForeignKey(reviews, on_delete=models.CASCADE,related_name='review')
    started=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.user}'s Favourite: {self.Favorite.title}"


class Comment(models.Model):
    review=models.ForeignKey(reviews, on_delete=models.CASCADE, related_name='comment')
    oneword=models.CharField(max_length=100)
    rating=models.PositiveSmallIntegerField(default=0,validators=[MaxValueValidator(5)])
    description=models.TextField()
    Name = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Name')

    def __str__(self):
        return f"commenting on {self.review.title}"

