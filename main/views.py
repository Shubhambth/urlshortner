# shortener/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ShortenedURL
from django.urls import reverse

def home(request):
    if request.method == "POST":
        original_url = request.POST.get('url')
        shortened = ShortenedURL.objects.create(original_url=original_url)
        short_url = request.build_absolute_uri(reverse('redirect_view', args=[shortened.short_path]))
        return render(request, 'home.html', {'short_url': short_url})
    return render(request, 'home.html')

def redirect_view(request, short_path):
    # Do not increment the visit count here
    url_obj = get_object_or_404(ShortenedURL, short_path=short_path)
    return render(request, 'landing_page.html', {
        'original_url': url_obj.original_url,
        'short_path': url_obj.short_path  # Pass short_path to the template
    })

def final_redirect_view(request, short_path):
    url_obj = get_object_or_404(ShortenedURL, short_path=short_path)
    url_obj.visits += 1  # Increment visits only when the button is clicked
    url_obj.save()
    return redirect(url_obj.original_url)



