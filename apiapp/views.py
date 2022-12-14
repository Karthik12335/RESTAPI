from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
import json
from apiapp.models import Studentinfo
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from apiapp.serializer import Studentserializer
# Create your views here.
'''
step1: Retrive data from the request (this is binary data)
step2: JSON to Byte object conversion 
step3: convert Byteobject to Dictionary or python native
step4: convert python native i.e dict into model instance or model object or table or record 
    Serializer
    ----------
    1. create serializer.py in the application folder
    2. import serializer for rest_framework
    3. define serializer class , similar to model class
    4. define create method, which return model instance
'''
@csrf_exempt

def insert_data(request):
    jbdata=request.body
    print(jbdata)
    jdata=io.BytesIO(jbdata)
    print(jdata)
    dict=JSONParser().parse(jdata)
    print(dict)
    s=Studentserializer(data=dict)
    print(s)
    if s.is_valid():
        s.save()
        d={'res':'Record inserted successfully'}
        j_res=json.dumps(d)

        return HttpResponse(j_res,content_type="application/json")


def get_all(request):
    if request.method=="GET":
        
        d=Studentinfo.objects.all()
        print(d)
        #convert modelinstance to dict by serializer
        s=Studentserializer(d,many=True)
        print(s.data)
        jdata=JSONRenderer().render(s.data)
        print(jdata)
        return HttpResponse(jdata,content_type="application/json")


def getstudent(request):
     
     if request.method=="GET":
        jdata=request.body
        print(jdata)
        sdata=io.BytesIO(jdata)
        print(sdata)
        dict=JSONParser().parse(sdata)
        rid=dict['id']
        print(rid)
        stu=Studentinfo.objects.get(id=rid)
        print(stu)
        s=Studentserializer(stu)
        print(s.data)
        jdata=JSONRenderer().render(s.data)
        print(jdata)
        return HttpResponse(jdata,content_type="application/json")


@csrf_exempt
def delete(request):
    
    if request.method=='DELETE':
        jdata=request.body
        print(jdata)
        sdata=io.BytesIO(jdata)
        print(sdata)
        dict=JSONParser().parse(sdata)
        rid=dict['id']
        print(rid)
        stu=Studentinfo.objects.get(id=rid)
        stu.delete()
        d={'res':'Record deleted successfully'}
        j_res=json.dumps(d)

        return HttpResponse(j_res,content_type="application/json")


@csrf_exempt

def get_update(request):

    if request.method=='PUT':
        jbdata=request.body
        print(jbdata)
        jdata=io.BytesIO(jbdata)
        print(jdata)
        dict=JSONParser().parse(jdata)
        rid=dict['id']
        stu=Studentinfo.objects.get(id=rid)
        s=Studentserializer(stu,data=dict,partial=True)

        if s.is_valid():
            s.save()
            d={'res':'Record Updated successfully'}
            j_res=json.dumps(d)

            return HttpResponse(j_res,content_type="application/json")
