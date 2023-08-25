from django.shortcuts import render
from .forms import  contact_form

def contact_view(request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = contact_form()
    context = {'form': form}
    return render(request, 'contact.html', context)