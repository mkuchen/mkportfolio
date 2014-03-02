from django.contrib.auth.models import User
from django.db import models

import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField

import urllib
import datetime

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^cloudinary\.models\.CloudinaryField"])

class Member(models.Model):
	user = models.OneToOneField(User)
	display_name = models.CharField(max_length=60, default="Referral Marketing Solutions")
	quote = models.CharField(max_length=300, default="Let's get things rolling!")
	bio = models.TextField(default="")
	profile_image = CloudinaryField("image", default=None, blank=True, null=True)

	def cropped_image(self):
		return self.logo_image.image( width = 150,  height = 150, 
			crop = "thumb", gravity = "face" )
