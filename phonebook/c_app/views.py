from django.shortcuts import render, redirect, get_object_or_404
from .models import  *
from .forms import *
# Create your views here.

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'contacts': contacts})

def view_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/view_contact.html', {'contact': contact})

def edit_contact(request, id):
    contact = get_object_or_404(Contact, pk=id)  # Fetch the contact based on the provided id
    if request.method == 'POST':
        # Handle form submission (e.g., save changes to the contact)
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        contact.email = request.POST['email']
        contact.save()
        return redirect('list_contacts')  # Redirect to the contact list page
    return render(request, 'contacts/edit_contact.html', {'contact': contact})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('list_contacts')

def call_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/call_contact.html', {'contact': contact})
