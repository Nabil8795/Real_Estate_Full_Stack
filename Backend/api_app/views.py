from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from api_app.models import Property
from api_app.serializers import PropertySerializer
from .models import Property
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PropertySerializer


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