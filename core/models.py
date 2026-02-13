from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class PricingPlan(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='plans')
    title = models.CharField(max_length=100)  # Basic / Standard / Premium
    price = models.CharField(max_length=50)   # "₹15,000" or "$199"
    duration = models.CharField(max_length=50, blank=True)  # per month / one-time
    features = models.TextField(help_text="One feature per line")
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.service.name} - {self.title}"

class Lead(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)

    email = models.EmailField()
    service = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    client_name = models.CharField(max_length=200)
    description = models.TextField()
    results = models.TextField()
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

