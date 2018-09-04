from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
from django.core.urlresolvers import reverse

class Post(models.Model):
    auth = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now())
    published_date = models.DateField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_commit(self):
        return  self.commits.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return  self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='commits')
    auth = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approved(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text