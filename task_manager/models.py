from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_comments')

    def __str__(self):
        return f"Comment by {self.created_by.username} on {self.task.title}"

class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dashboard')
    tasks = models.ManyToManyField(Task, related_name='dashboards')

@receiver(post_save, sender=User)
def create_dashboard(sender, instance, created, **kwargs):
    if created:
        Dashboard.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_dashboard(sender, instance, **kwargs):
    instance.dashboard.save()

class taskmanager_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username