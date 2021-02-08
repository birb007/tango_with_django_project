from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.
class Category(models.Model):
    NAME_MAX_LEN = 128
    VIEWS_INIT = LIKES_INIT = 0

    name = models.CharField(max_length=NAME_MAX_LEN, unique=True)
    views = models.IntegerField(default=VIEWS_INIT)
    likes = models.IntegerField(default=LIKES_INIT)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LEN = 128
    VIEWS_INIT = 0

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LEN)
    url = models.URLField()
    views = models.IntegerField(default=VIEWS_INIT)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to="profile_images", blank=True)

    def __str__(self):
        return self.user.name

