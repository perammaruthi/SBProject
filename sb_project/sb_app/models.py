from django.contrib.auth.models import User
from django.db import models
from django.db.models import JSONField
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    address = models.TextField(null=True, blank=True)
    zip_code = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

class Services(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    details = JSONField(default=dict)
