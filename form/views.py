from django.shortcuts import render


# Create your views here.
def selection_form(request):
    return render(request, 'form/selection_form.html', {})
