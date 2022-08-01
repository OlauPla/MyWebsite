from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Contact

MANTENIMIENTO = False #maintenence mode
def index(request):

    if MANTENIMIENTO == True:
        return render(request, 'main/maintenence.html')

    else:
        if request.POST:
            f = ContactForm(request.POST)
            if f.is_valid():
                messages.success(request, "Message sent successfuly!")
                name = f.cleaned_data["name"]
                email = f.cleaned_data["email"]
                message = f.cleaned_data["message"]
                contact = Contact(name=name,email=email,message=message)
                contact.save()
                return redirect('/#contact')
                
                

        else:
            f = ContactForm()

        return render(request, 'main/index.html', { 'form': f })

