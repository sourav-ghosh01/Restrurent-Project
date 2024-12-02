from django.db import models

# Create your models here.
class Item_list(models.Model):
    Category_name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.Category_name
    

class Items(models.Model):
    Item_name = models.CharField(max_length=20)
    description = models.TextField(max_length=150,blank=False)
    Price = models.TextField(max_length=30)
    Category = models.ForeignKey(Item_list,related_name='Name',on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='items/')
    
    def __str__(self):
        return self.Item_name 

class AboutUs(models.Model):
    Description = models.TextField(max_length=150,blank=False)

class Book_Table(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()    
    
    
    def __str__(self):
        return self.Name
