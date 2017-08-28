# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(default=None, blank=True, null=True, max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Description(models.Model):
	desc = models.CharField(max_length=255)
	describer = models.OneToOneField(Course, related_name = "course_desc")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
