from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404
from .models import Produce as Produce, Type
from .forms import Product,SearchForm

# Create your views here.
def index(req):
    pp = Produce.objects.all()
    return render(req, 'myweb/index.html',{'pp':pp})


#---------------search------------------------

def search(req):
    if req.method == "POST":
        form = SearchForm(req.POST)
        if form.is_valid():
            searchby = str(form.cleaned_data['SearchBy'])

            if searchby == 'Alldum':
                showType = Produce.objects.filter(TypeName__Type_Name__contains=searchby)

            elif searchby == 'Card':

                showType = Produce.objects.filter(TypeName__Type_Name__contains=searchby)


            elif searchby == 'Photobook':

                showType = Produce.objects.filter(TypeName__Type_Name__contains=searchby)


            elif searchby == 'Poster':

                showType = Produce.objects.filter(TypeName__Type_Name__contains=searchby)

            return render(req , "myweb/showsearch.html",{"showType":showType})
    else:
        form = SearchForm()
        context = {'form':form}
        return render(req, 'myweb/search.html',context)

#----------------------------------------------------------------------

def indexuser(req):
    pp = Produce.objects.all()
    return render(req, 'myweb/indexuser.html',{'pp':pp})

def Write(req):
	pp = Produce.objects.all()
	ins = {
        'pp' : pp
        }
	return render(req,'myweb/Write.html', ins)

def Productss(req):
    pp = Produce.objects.all()
    return render(req, 'myweb/Product.html',{'pp':pp})

def Login(req):
    return render(req, 'myweb/Login.html')

def detail(request, question_id):
    return render(request, 'myweb/detail.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def Register(req):
    return render(req, 'myweb/Register.html')

def ProductPlus(req):
    return render(req, 'myweb/ProductPlus.html')

#-------------register-----------------
def Register(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f"New account created: {username}")
            login(req, user)
            return redirect("/indexuser")

        else:
            for msg in form.error_messages:
                messages.error(req, f"{msg}: {form.error_messages[msg]}")

            return render(req,
                          template_name = "myweb/Register.html",
                          context={"form":form})
    form = UserCreationForm(req.POST)
    return render(req,
                template_name = "myweb/Register.html",
                context={"form":form})

#-------------- login ------------------------

def Login(req):
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                messages.info(req, f"You are now logged in as {username}")
                return redirect('/indexuser')
            else:
                messages.error(req, "Invalid username or password.")
        else:
            messages.error(req, "Invalid username or password.")
    form = AuthenticationForm()
    return render(req,
                  template_name = "myweb/Login.html",
                  context={"form":form})


#---------------logout-------------------

def logout(req):
    logout(req)
    messages.info(req, "Logged out successfully!")
    return redirect("/index")

#---------------Write-----------------

def Write(request):
    if request.method == 'POST':
        form = Product(request.POST)

        if form.is_valid():
            p = form.save()
            p.save()
            return redirect("/indexuser")
    else:
        form = Product()
        context = {'form': form}
        return render(request, 'myweb/Write.html', context)