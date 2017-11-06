from django.conf import settings
from django.contrib.auth.models import User

class TwitterBackend:

    def my_view(request):
        username = None
        if request.user.is_authenticated():
            username = request.user.username


