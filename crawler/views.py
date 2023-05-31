import requests
import csv
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from .models import Website, Page, Link


# Create your views here.

def crawl(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        website = Website.objects.get_or_create(url=url)[0]
        
        # Fetch the web page
        response = requests.get(url)
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract page title and content
        title = soup.title.string if soup.title else ''
        content = soup.get_text()
        
        # Create a new page object
        page = Page.objects.create(website=website, url=url, title=title, content=content)
        
        # Find all links on the page and create link objects
        for link in soup.find_all('a'):
            link_url = link.get('href')
            if link_url:
                Page.objects.get_or_create(website=website, url=link_url)
                Link.objects.create(from_page=page, to_page=Page.objects.get(url=link_url))
        
        # Update the last_crawled field of the website
        website.last_crawled = page.crawled_at
        website.save()
        
        # Write data to CSV
        write_to_csv(page)

        return redirect('show_pages')
    
    return render(request, 'crawler/crawl.html')

def show_pages(request):
    pages = Page.objects.all()
    return render(request, 'crawler/show_pages.html', {'pages': pages})

def write_to_csv(page):
    fieldnames = ['url', 'title', 'content']
    filename = 'crawled_data.csv'

    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:  # Check if the file is empty
            writer.writeheader()

        writer.writerow({
            'url': page.url,
            'title': page.title,
            'content': page.content
        })