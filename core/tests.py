from django.test import TestCase

# Create your tests here.
class UserProfile(models.Model):
    user = models.CharField(max_length=100)
    stripe_customer_id = models.CharField(max_length=50)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
