from django.db import models
from django.contrib.auth.models import User

# User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profiles/')

# Property / Room Model (MOST IMPORTANT)
class Property(models.Model):

    ROOM_TYPES = (

        ('PG', 'PG'),

        ('Flat', 'Flat'),

        ('Hostel', 'Hostel'),

        ('Apartment', 'Apartment'),

        ('Room', 'Room'),

    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    description = models.TextField()

    price = models.IntegerField()

    location = models.CharField(max_length=200)

    room_type = models.CharField(max_length=20, choices=ROOM_TYPES,default='Room')

    furnished = models.BooleanField(default=False)

    available = models.BooleanField(default=True) 

    image = models.ImageField(upload_to='properties/')

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

   

# Property Image Model
class PropertyImage(models.Model):

    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='property_images/')

# Contact / Inquiry Model
class Inquiry(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=10,default='9999999999')

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Review Model (Optional but Good)
class Review(models.Model):

    # property = models.ForeignKey(Property, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
