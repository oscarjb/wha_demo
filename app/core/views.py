from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

from wha_products.models import Company

# Create your views here.

class Index(View):
    template = 'core/index.html'

    def get(self, request):
        
        company = {}
        if Company.objects.filter(user_company=request.user):
            company = Company.objects.filter(user_company=request.user)[0]
        
        return render(request, self.template, {"company" : company})

class Register_user(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "core/register.html", {'form': form})

    def post(self, request):
        
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, "core/register.html", {'form': form})

def handle_not_found(request, exception):
    return render(request, "core/404.html")