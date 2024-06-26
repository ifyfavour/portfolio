from django.shortcuts import render, redirect
from .models import Service, PortfolioImage
from .forms import ServiceForm, PortfolioImageForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    services = Service.objects.all()
    images = PortfolioImage.objects.all()
    return render(request, 'index.html', {'services': services, 'images': images})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ServiceForm()
    return render(request, 'add_service.html', {'form': form})
@login_required(login_url='/')
def add_image(request):
    if request.method == 'POST':
        form = PortfolioImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PortfolioImageForm()
    return render(request, 'add_image.html', {'form': form})

