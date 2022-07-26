from ast import parse
import json
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.urls import is_valid_path
from . forms import AddService
from . models import User_service
from . serializers import User_service_serializer

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'GET':
        user_detail = User_service.objects.all()
        serializer = User_service_serializer(user_detail, many = True)
        data = json.dumps(serializer.data)
        json_data = json.loads(data)
        print(type(json_data))
        return render(request, 'myapp/index.html', {'userdata':json_data})
        # return JsonResponse(data, safe=False)

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = User_service_serializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = { 'msg' : 'Record Added' }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json' )
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json' )

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        user = User_service.objects.get(id=id)
        serializer = User_service_serializer(user, data = pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = { 'msg' : 'Data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        user = User_service.objects.get(id = id)
        user.delete()
        res = { 'msg' : 'Data deleted' }
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')



def home(request):
    if request.method == 'POST':
        fm = AddService(request.POST)
        if fm.is_valid():
            fm.save()
        fm = AddService()
    else:
        fm = AddService()
    return render(request, 'myapp/home.html', {'fm':fm})