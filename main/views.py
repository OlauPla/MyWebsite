from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def index(request):
    if request.POST:
        f = ContactForm(request.POST)
        if f.is_valid():
            messages.success(request, "Message sent successfuly!")
            return redirect('home')
            
            

    else:
        f = ContactForm()

    return render(request, 'main/index.html', { 'form': f })