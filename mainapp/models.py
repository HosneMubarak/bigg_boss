from django.db import models


# Create your models here.
class ChoiceProgram(models.Model):
    program_name = models.CharField(max_length=400)

    def __str__(self):
        return self.program_name


class Article(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, unique=True)

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    program = models.ForeignKey(ChoiceProgram, on_delete=models.CharField)
    created = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    single_video_google = models.URLField(max_length=400, blank=True, null=True)
    single_video_other = models.URLField(max_length=400, blank=True, null=True)

    Part_1 = models.URLField(max_length=400, blank=True, null=True)
    Part_2 = models.URLField(max_length=400, blank=True, null=True)
    Part_3 = models.URLField(max_length=400, blank=True, null=True)
    Part_4 = models.URLField(max_length=400, blank=True, null=True)
    Part_5 = models.URLField(max_length=400, blank=True, null=True)
    Part_6 = models.URLField(max_length=400, blank=True, null=True)

    Ad_link_1 = models.URLField(max_length=400, blank=True, null=True)
    Ad_link_2 = models.URLField(max_length=400, blank=True, null=True)
    Ad_link_3 = models.URLField(max_length=400, blank=True, null=True)
    Ad_Part_link = models.URLField(max_length=400, blank=True, null=True)

    published = models.BooleanField(default=False)
    publish_date = models.DateField(auto_now=False, blank=False, null=True)

    ad_published = models.BooleanField(default=False)

    slug = models.SlugField(unique_for_date='publish_date')

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=40, blank=True, default='BB User')
    text = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.author
