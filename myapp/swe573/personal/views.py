from django.contrib.auth.decorators import login_required
from django.shortcuts import render

#def index(request):
 #   return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me','selingungor01@gmail.com']})

@login_required
def index(request):
    return render(request, 'personal/home.html')