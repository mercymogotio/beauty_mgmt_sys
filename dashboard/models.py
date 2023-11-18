from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Service
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='uploads/productImg')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_products_count():
    	return Product.objects.count() 
    

class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=8, null=True)
    mobile = models.CharField(max_length=15)
    image = models.ImageField(upload_to='staffImages', default='path_to_default_image.jpg')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Assuming Service is another model
    # rating = models.ForeignKey(Rating, on_delete=models.CASCADE)  # You would need to create a Rating model
#
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_staffs():
        return Staff.objects.all()

    @staticmethod
    def get_staffs_count():
    	return Staff.objects.count()


    @staticmethod
    def get_staff_by_email(email):
        try:
            return Staff.objects.get(email = email)
        except:
            return False

    def isExists(self):
        if Staff.objects.filter(email = self.email):
            return True
        return False
class Rating(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.TextField(blank=True, null=True)

    @property
   
    def average_rating(self):
        ratings = Rating.objects.filter(staff=self.staff)
        total_ratings = sum(rating.rating for rating in ratings)
        count_ratings = len(ratings)

        if count_ratings > 0:
            return total_ratings / count_ratings
        else:
            return 0
