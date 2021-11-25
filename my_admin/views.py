from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group, User


def enter_view(request):
    return HttpResponseRedirect('animal/animal/')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['cod'] == 'aFb2ls5vn':
                email = form.cleaned_data['email']
                user = User.objects.all().filter(email=email)
                if user.exists():
                    messages.error(request, "Adresa de email este deja folosită!")
                    return HttpResponseRedirect('/register')
                else:
                    new_user = form.save()
                    my_group, created = Group.objects.get_or_create(name='Medic')
                    my_group.user_set.add(new_user)
                    new_user = authenticate(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            )
                    login(request, new_user)
                    return HttpResponseRedirect('/')
            else:
                return HttpResponseForbidden()

    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'admin/register.html', args)
