from django.shortcuts import render
from .models import Showcase


# Create your views here.
def showcase_index(request):
    showcases = Showcase.objects.all()
    context = {
        'showcase': showcases
    }
    return render(request, 'showcase_index.html', context)

def showcase_detail(request, pk):
    showcase = Showcase.objects.get(pk=pk)
    context = {
        'showcase': showcase
    }
    return render(request, 'showcase_detail.html', context)
