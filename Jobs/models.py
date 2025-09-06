from django.db import models
from django.conf import settings
from django.core .validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"
    
class Job(models.Model):
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    requirements=models.TextField()
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    published_date=models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category_names')
 
    def __str__(self):
        return f"{self.title} {self.description}"
    
    
class jobApplication(models.Model):
   job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name='applications')
   applicant =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
   resume=models.FileField(upload_to='resume/')
   Name=models.CharField(max_length=50)
   portfolio_link = models.URLField(max_length=500, blank=True, null=True)   
   applied_at=models.DateField(auto_now_add=True)
   status_choices = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
   status = models.CharField(max_length=10, choices=status_choices, default='pending')
   def __str__(self):
        return f"{self.applicant.email} - {self.job.title}"

class Review(models.Model):
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews_received')
    job_seeker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews_given')
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])   
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='reviews')  # new
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_seeker} -> {self.employer} ({self.rating})"
   
   
    