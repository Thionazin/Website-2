from django.shortcuts import render

# Create your views here.
def academics(request):
    return render(request, 'a_and_a.html', {})
