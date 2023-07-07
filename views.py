from django.shortcuts import render, redirect
from django.http import JsonResponse
from .scrap import WebScraper

def index(request):
    return render(request, 'index.html')

def process_form(request):
    if request.method == 'POST':
        query = request.POST.get('name')  # Get the user's query from the form
        url = request.session.get('url')  # Get the scraped URL from the session
        
        # Perform any processing or analysis on the query and scraped data
        # Generate captions or responses based on the query and scraped data
        
        # Example: Generating a response based on the query
        response = f"You entered: {query}. Captions or responses can be generated based on the scraped data."
        
        return render(request, 'index.html', {'response': response})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def scrap_view(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        scraper = WebScraper(url)
        data = scraper.scrape()  # Scraping the website data
        with open('data.txt', 'w') as file:
            file.write(data)  # Saving the data to a file
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
