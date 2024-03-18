from django.shortcuts import render, HttpResponse, redirect
from rest_framework import viewsets
from api_app.models import Property
from api_app.serializers import PropertySerializer
from .models import Property
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PropertySerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def index(request):
    return render(request, 'index.html')

def all_prop(request):
    props = Property.objects.all()
    context = {
        'props': props
    }
    return render(request, 'view_all_prop.html', context)

def add_prop(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = int(request.POST['price'])
        detail = request.POST['detail']
        image = request.POST['image']
  
#        image_file = request.FILES['image']
#        image=Image.open(image_file)
#        image_path = 'static/' + image.name
#        image.save(image_path)

    
        new_prop=Property(name=name, price=price, detail=detail, image=image) 
        new_prop.save()
        return HttpResponse("Property added successfully")
    else:
        return render(request, 'add_prop.html')
    

def remove_prop(request ,prop_id=0):
    props = Property.objects.all()
    context = {
            'props': props
        }  
    if prop_id:
        try:
            prop_to_remove=Property.objects.get(id=prop_id)
            prop_to_remove.delete()
            return HttpResponse("Property removed successfully")
        except:
            return HttpResponse("Select valid Name")
    else:
        return render(request, 'remove_prop.html', context)

def filter_prop(request):
    if request.method== 'POST':
        name = request.POST['name']
        price = request.POST['price']
        prop= Property.objects.all()
        if name:
            prop = prop.filter(name__icontains = name)

        if price:
            prop = prop.filter(price__icontains = price)

        context = {
            'props':prop
        }
        return render(request, 'view_all_prop.html', context)
    
    else:
        return render(request, 'filter_prop.html')

@api_view(['POST', 'GET'])
def Proper(request):
    objs = Property.objects.all()
    serializer = PropertySerializer(objs, many = True)
    return Response(serializer.data)

## User Authentication
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')