from django.db import models

class Booking(models.Model):
    ID = models.AutoField(primary_key=True, auto_created=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking Records'

    def __str__(self):
        return f"{self.Name} with {self.No_of_guests} guests on {self.BookingDate}" 
    

class Menu(models.Model):
    ID = models.AutoField(primary_key=True, auto_created=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return f"{self.Title} {self.Price} {self.Inventory}"
      
