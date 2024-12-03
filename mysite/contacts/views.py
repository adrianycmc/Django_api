from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import NameForm, ContactForm
from django.urls import reverse



def create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form .is_valid():
            instance = form.save()
            return HttpResponseRedirect(reverse("contacts:thanks", args=(instance.sender, )))
    else:
        form = ContactForm()
    return render(request, "contacts/create.html", {"form": form})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data["your_name"]
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('contacts:thanks', args=(name, )))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "contacts/name.html", {"form": form})

def thanks(request, name):
    return HttpResponse(f"Obrigado por preencher o formulário, {name}!")