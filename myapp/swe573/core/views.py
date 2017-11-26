from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.views.generic import TemplateView
from django.shortcuts import render, reverse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from core.forms import HomeForm
from social_django.models import UserSocialAuth
from core.models import Post
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = authenticate(
#                 username=form.cleaned_data.get('username'),
#                 password=form.cleaned_data.get('password1')
#             )
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})


template_name = 'core/home.html'


@login_required
def home(request):
    form = HomeForm()
    return render(request, template_name, {'form': form})


@login_required
def post_create(request):
    form = HomeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        Post.objects.all().delete()
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Success.')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'core/home.html', context)

# @login_required
# def home(request):
#     return render(request, 'core/home.html')


@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None
    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None
    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'core/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'core/password.html', {'form': form})


def getUser(request):
    if request.method == 'POST':
        current_user = request.user
        print(current_user.id)
    return current_user