from django.db import models
from django.contrib.auth.models import User


class customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    customer_name = models.ForeignKey(customer, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status_choices = (
        ('open', 'Open'),
        ('closed', 'Closed'),
    )
    status = models.CharField(max_length=10, choices=status_choices, default='open')

    def __str__(self):
        return self.title


class comment(models.Model):
    ticket = models.ForeignKey(ticket, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.ticket.title}"
    
class ticket_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    