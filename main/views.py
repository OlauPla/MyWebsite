from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    if request.POST:
        f = ContactForm(request.POST)
        if f.is_valid():
            return redirect('home')
            

    else:
        f = ContactForm()

    return render(request, 'main/index.html', { 'form': f })