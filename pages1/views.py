from django.shortcuts import render
from pages1.models import Profession
def index_page(request):
    data = {
        'proffession': Profession.objects.get(id=1)
    }
    return render(request, 'index.html', context=data)

# Create your views here.
