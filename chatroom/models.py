from django.db import models
from django.contrib.auth.models import User

class Chats(models.Model):
	user_from = models.ForeignKey(User)
	channel = models.CharField(max_length=255)
	message = models.CharField(max_length=255)
