from django.contrib import admin
from .models import Job,jobApplication,Category,Review
# Register your models here.
admin.site.register(Job)
admin.site.register(jobApplication)
admin.site.register(Category)
admin.site.register(Review)

