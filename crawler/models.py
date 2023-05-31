from django.db import models

# Create your models here.

class Website(models.Model):
    url = models.URLField(unique=True)
    last_crawled = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.url

class Page(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    url = models.URLField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    crawled_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Link(models.Model):
    from_page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='outgoing_links')
    to_page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='incoming_links')
    
    def __str__(self):
        return f'From: {self.from_page} | To: {self.to_page}'

