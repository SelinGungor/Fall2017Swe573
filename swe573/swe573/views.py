from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def contact(request):
   return render(request, 'contact.html')


def about_deepyou(request):
   return render(request, 'about_deepyou.html')