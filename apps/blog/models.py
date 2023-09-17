from django.db import models
from apps.user_system.models import Model_users
from ckeditor.fields import RichTextField
from django.utils.text import slugify



class Categoryes (models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"slug{self.name}slug")
            self.slug.lower()
        self.name = self.name.capitalize()
        super().save(*args, **kwargs)
      

class Blogs (models.Model):

    class Meta:
        ordering = ["-creation"]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    img = models.ImageField(upload_to="img_blogs", blank=True)
    content = RichTextField(config_name='ckeditor')
    views = models.IntegerField(default=0)
    public = models.BooleanField(default=False)
    creation = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    user = models.ForeignKey(Model_users, models.CASCADE, null=True)
    category = models.ForeignKey(Categoryes, models.PROTECT, null=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"slug{self.title.lower()}"
        self.description = self.description.capitalize()
        super().save(*args, **kwargs)
