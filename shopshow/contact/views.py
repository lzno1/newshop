from django.shortcuts import render
from .models import FAQuestion

# Create your views here.
def contact(request):
    questions = FAQuestion.objects.all()
    return render(request, 'contact.html', {'faqs':questions})